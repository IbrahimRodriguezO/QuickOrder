from django.urls import path
from . import views

app_name = "chef_app"

urlpatterns = [
    path('ordenes/', views.ChefPage.as_view(), name="panel-chef")
]