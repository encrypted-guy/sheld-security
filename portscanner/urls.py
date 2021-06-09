from django.urls import path
from . import views


urlpatterns = [
    path('port-scan', views.search, name='portscan'),
    path('port-scan-result', views.result, name="portscan_result")
]