from django.urls import path
from . import views


urlpatterns = [
    path('nslookup-scan', views.nslookup_scan, name='nslookup'),
    path('nslookup-scan-result', views.nslookup_result, name="nslookup_result"),

    path('traceroute-scan', views.traceroute_scan, name='traceroute'),
    path('traceroute-scan-result', views.traceroute_result, name="traceroute_result"),
    
    path('whois-scan', views.whois_scan, name='whois'),
    path('whois-scan-result', views.whois_result, name="whois_result")
] 