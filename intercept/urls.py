from django.urls import path
from . import views


urlpatterns = [
    path('intercept-scan', views.scanner, name='intercept'),
    path('intercept-scan-result', views.result, name="intercept_result")
]