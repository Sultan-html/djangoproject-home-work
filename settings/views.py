from django.shortcuts import render
from settings.models import Employee

def nok(request):       
    employee = Employee.objects.latest("id")
    return render(request, "index.html", locals())

def gokgok(request):
    tixt = {
        'title': "Babil",
        "description": "Babil black",
        "bobo": "SILDEREI"
    }
    return render(request, 'index.html', context=tixt)