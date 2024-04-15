from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.signing import Signer
from .models import Sheet
from .forms import SheetForm, ApiForm
import pandas as pd
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def sheet_home(request):
    if request.user.is_superuser:
        sheet_list = list(Sheet.objects.values("id", "name", "records_length"))
    else:
        sheet_list = list(Sheet.objects.values("id", "name", "records_length").filter(user=request.user.id))

    sheet_list.sort(key=lambda x: x["id"])
    return render(request, "sheet/sheet.html", {"sheet":"", "sheet_list":sheet_list, "form": SheetForm(), "api_form": ApiForm()})

def load_sheet_data(sheet_url):
    df = pd.read_csv(sheet_url, dtype="string")
    df.fillna("", inplace=True)
    table = df.to_dict(orient='records')
    
    return json.dumps(table)

@login_required
def refresh_sheet(request, id_sheet):
    sheet = Sheet.objects.get(id = id_sheet)
    
    sheet.data = load_sheet_data(sheet.url)
    sheet.records_length = len(json.loads(sheet.data))

    sheet.save()

    return redirect("sheet_home")

@login_required
def create_sheet(request):
    if request.method == "POST":
        sheet = Sheet(
            name=request.POST["name"],
            url=request.POST["url"],
            user=User.objects.get(id=request.user.id)
        )

        sheet.data = load_sheet_data(sheet.url)
        sheet.records_length = len(json.loads(sheet.data))

        sheet.save()

        return redirect("sheet_home")

@login_required
def get_sheet(request, id):
    sheet = Sheet.objects.values("id", "name", "url", "api_url", "api_isactive").get(id=id)

    sheet_dict = {
        "id": sheet["id"],
        "name": sheet["name"],
        "url": sheet["url"],
        "api_url": sheet["api_url"],
        "api_isactive": sheet["api_isactive"]
    }

    return HttpResponse(json.dumps(sheet_dict), "application/json")

@login_required
def update_sheet(request):
    if request.method == "POST":
        sheet = Sheet.objects.get(id=request.POST["id"])

        sheet.name = request.POST["name"]
        sheet.url = request.POST["url"]

        sheet.data = load_sheet_data(sheet.url)
        sheet.records_length = len(json.loads(sheet.data))

        sheet.save()

        return redirect("sheet_home")

def get_sheet_data(request, name, api_password, id_sheet):
    request.user = User.objects.get(username=name)
    signer = Signer()

    sheet = Sheet.objects.get(id = id_sheet)

    try:
        signer.unsign(f"{api_password}:{sheet.api_password}")
    except:
        raise Http404()

    if sheet.api_isactive == False or sheet.user.id != request.user.id:
        raise Http404()

    data = json.loads(sheet.data)

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

@login_required
def active_api(request):
    if request.method == "POST":
        sheet = Sheet.objects.get(id = request.POST["id"])
        signer = Signer()
        (password, signed_password) = signer.sign(request.POST["api_password"]).split(":")
        sheet.api_password = signed_password
        sheet.api_isactive = True
        sheet.api_url = f"{request.META['wsgi.url_scheme']}://{request.META['HTTP_HOST']}/sheet/api/{request.user.username}:password/data/{sheet.id}"

        sheet.save()

        return redirect("sheet_home")