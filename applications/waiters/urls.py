from django.urls import path
from . import views

app_name = "waiter_app"

urlpatterns = [
    path('pedidos/', views.WaiterPage.as_view(), name="panel-waiter"),
    path('platillos/<int:mesa>', views.ListaMenu, name="platillos-menu")
]