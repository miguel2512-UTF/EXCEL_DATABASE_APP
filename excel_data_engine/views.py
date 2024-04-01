from django.shortcuts import render, redirect
from .models import Excel
from .forms import ExcelForm
import pandas as pd
import math

def excel_home(request):
    excel_list = list(Excel.objects.values())
    return render(request, "excel/excel.html", {"excel":"", "excel_list":excel_list, "form": ExcelForm()})

def excel_app(request, name):
    excel = Excel.objects.get(name = name)
    if excel.refresh:
        url = excel.url
        df = pd.read_csv(url)
        table = df.to_dict(orient='records')
        jsonTable = df.to_json(orient='records')
        excel.data = jsonTable
        excel.refresh = False
        excel.save()
        print(table)
    else:
        table = json.loads(excel.data)

    column_names = table[0].keys()
    column_names = list(column_names)

    NoneType = type(None)
    for index in range(len(table)):
        for key in column_names:
            if type(table[index][key]) == float:
                if math.isnan(table[index][key]):
                    table[index][key] = ''
            elif type(table[index][key]) == NoneType:
                table[index][key] = ''

    filter_columns=[]
    for key in column_names:
        column_key = re.sub('[^A-Za-z0-9]+', '', key)
        filter_columns.append(column_key)

    return render(request, "excel/excel-spreadsheet.html", {
        "excel": table,
        "column_names": column_names,
        "id_columns": filter_columns,
        "excel_data": excel
    })

def refresh_excel(request, name):
    excel = Excel.objects.get(name = name)
    excel.refresh = True
    excel.save()

    return redirect(f"/excel/spreadsheet/{name}")