from django.urls import path, re_path,include
from . import views

app_name = "owner_app"

urlpatterns = [
    path('panel/', views.HomePage.as_view(), name="panel"),
    path('panel_menu/', views.ListMenu.as_view(), name="panel-menu"),
    path('panel_menu/<pk>/', views.MenuDeleteView.as_view(), name="eliminar-platillo"),
    path('agregar-platillo/', views.MenuCreateView.as_view(), name='agregar-platillo'),
    path('editar-platillo/<int:pk>/', views.MenuUpdateView.as_view(), name='editar-platillo'),
    path('lista_usuarios/', views.ListUser.as_view(), name="lista-usuarios"),
    path('crear_usuario/', views.UserCreateView.as_view(), name="crear-usuario"),
]