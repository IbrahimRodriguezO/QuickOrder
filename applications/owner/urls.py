from django.urls import path, re_path,include
from . import views

app_name = "owner_app"

urlpatterns = [
    path('panel/', views.HomePage.as_view(), name="panel")
]