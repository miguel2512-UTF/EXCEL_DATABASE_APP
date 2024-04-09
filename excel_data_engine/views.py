from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.signing import Signer
from .models import Excel
from .forms import ExcelForm, ApiForm
import pandas as pd
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def excel_home(request):
    if request.user.is_superuser:
        excel_list = list(Excel.objects.values("id", "name", "records_length"))
    else:
        excel_list = list(Excel.objects.values("id", "name", "records_length").filter(user=request.user.id))

    excel_list.sort(key=lambda x: x["id"])
    return render(request, "excel/excel.html", {"excel":"", "excel_list":excel_list, "form": ExcelForm(), "api_form": ApiForm()})

def load_sheet_data(sheet_url):
    df = pd.read_csv(sheet_url, dtype="string")
    df.fillna("", inplace=True)
    table = df.to_dict(orient='records')
    
    return json.dumps(table)

def refresh_excel(request, id_sheet):
    excel = Excel.objects.get(id = id_sheet)
    
    excel.data = load_sheet_data(excel.url)
    excel.records_length = len(json.loads(excel.data))

    excel.save()

    return redirect("excel_home")

def create_excel(request):
    if request.method == "POST":
        excel = Excel(
            name=request.POST["name"],
            url=request.POST["url"],
            user=User.objects.get(id=request.user.id)
        )

        excel.data = load_sheet_data(excel.url)
        excel.records_length = len(json.loads(excel.data))

        excel.save()

        return redirect("excel_home")

def get_excel(request, id):
    excel = Excel.objects.values("id", "name", "url", "api_url", "api_isactive").get(id=id)

    excel_dict = {
        "id": excel["id"],
        "name": excel["name"],
        "url": excel["url"],
        "api_url": excel["api_url"],
        "api_isactive": excel["api_isactive"]
    }

    return HttpResponse(json.dumps(excel_dict), "application/json")

def update_excel(request):
    if request.method == "POST":
        excel = Excel.objects.get(id=request.POST["id"])

        excel.name = request.POST["name"]
        excel.url = request.POST["url"]

        load_images = request.POST.get("load_images", False)
        if load_images:
            excel.loadImages = True
        else:
            excel.loadImages = load_images

        excel.data = load_sheet_data(excel.url)
        excel.records_length = len(json.loads(excel.data))

        excel.save()

        return redirect("excel_home")

def get_sheet_data(request, name, api_password, id_sheet):
    request.user = User.objects.get(username=name)
    signer = Signer()

    excel = Excel.objects.get(id = id_sheet)

    try:
        signer.unsign(f"{api_password}:{excel.api_password}")
    except:
        raise Http404()

    if excel.api_isactive == False or excel.user.id != request.user.id:
        raise Http404()

    data = json.loads(excel.data)

    if request.GET:
        fields = data[0].keys()
        for field in fields:
            param = request.GET.get(field, "null")
            data = [ record for record in data if record[field] == param ] if param != "null" else data
    else:
        body = json.loads(request.body) if request.body else {}
        for key in body.keys():
            value = body[key]
            try:
                data = [ record for record in data if record[key] == value ]
            except KeyError:
                res = {
                    "success": False,
                    "error": f"No column found with name {key}"
                }
                return HttpResponse(json.dumps(res), content_type="application/json", status=400)

    res = {
        "success": True,
        "results_length": len(data),
        "results": data
    }

    return HttpResponse(json.dumps(res), content_type = "application/json")

def active_api(request):
    if request.method == "POST":
        excel = Excel.objects.get(id = request.POST["id"])
        signer = Signer()
        (password, signed_password) = signer.sign(request.POST["api_password"]).split(":")
        excel.api_password = signed_password
        excel.api_isactive = True
        excel.api_url = f"{request.META['wsgi.url_scheme']}://{request.META['HTTP_HOST']}/excel/api/{request.user.username}:password/data/{excel.id}"

        excel.save()

        return redirect("excel_home")

def test(request, name):
    return HttpResponse("Hola "+name)