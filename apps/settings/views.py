from django.shortcuts import render
from apps.settings.models import Basesettings
# Create your views here.

def settings(request):
    setting = Basesettings.objects.latest('id')
    return render(request, 'index.html', locals())
