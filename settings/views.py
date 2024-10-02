from django.shortcuts import render

# Create your views here.
# def settings(request):
#     context = {
#         'title': "Главное",
#         "description": "Байбол негр",
#         "bobo": "SILDEREI"
#     }
    # return render(request, 'index.html', context=context)

def gokgok(request):
    tixt = {
        'title': "Babil",
        "description": "Babil black",
        "bobo": "SILDEREI"
    }
    return render(request, 'index.html', context=tixt)