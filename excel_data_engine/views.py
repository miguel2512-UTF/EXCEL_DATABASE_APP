from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Excel
from .forms import ExcelForm
import pandas as pd
import math
import json

def excel_home(request):
    excel_list = list(Excel.objects.values("id", "name", "records_length"))
    excel_list.sort(key=lambda x: x["id"])
    return render(request, "excel/excel.html", {"excel":"", "excel_list":excel_list, "form": ExcelForm()})

def load_sheet_data(sheet_url):
    df = pd.read_csv(sheet_url)
    table = df.to_dict(orient='records')

    column_names = table[0].keys()
    column_names = list(column_names)

    NoneType = type(None)
    for index in range(len(table)):
        for key in column_names:
            if type(table[index][key]) == float:
                if math.isnan(table[index][key]):
                    table[index][key] = ''
                table[index][key] = math.trunc(table[index][key]) if type(table[index][key]) != str else table[index][key]
            elif type(table[index][key]) == NoneType:
                table[index][key] = ''
    
    return json.dumps(table)

def refresh_excel(request, id_sheet):
    excel = Excel.objects.get(id = id_sheet)
    
    excel.data = load_sheet_data(excel.url)
    excel.records_length = len(json.loads(excel.data))

    excel.save()

    return redirect("excel_home")

def create_excel(request):
    if request.method == "POST":
        load_images = request.POST.get("load_images", False)
        load_images = True if load_images else False
        excel = Excel(
            name=request.POST["name"],
            url=request.POST["url"],
            loadImages=load_images
        )

        excel.data = load_sheet_data(excel.url)
        excel.records_length = len(json.loads(excel.data))

        excel.save()

        return redirect("excel_home")

def get_excel(request, id):
    excel = Excel.objects.values("id", "name", "url").get(id=id)

    excel_dict = {
        "id": excel["id"],
        "name": excel["name"],
        "url": excel["url"],
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

def get_sheet_data(request, id_sheet):
    excel = Excel.objects.get(id = id_sheet)
    data = json.loads(excel.data)
    fields = data[0].keys()
    for field in fields:
        param = request.GET.get(field, "")
        data = [ record for record in data if record[field] == param ] if param != "" else data

    res = {
        "length": len(data),
        "results": data
    }

    return HttpResponse(json.dumps(res), content_type = "application/json")