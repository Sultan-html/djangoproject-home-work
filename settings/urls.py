from django.urls import path

# from settings.views import settings
from settings.views import gokgok

# urlpatterns = [
#     path('', settings, name='settings')
# ]

urlpatterns = [
    path('', gokgok, name='gokgok')
]