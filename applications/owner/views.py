from urllib import request
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView, FormView
from .models import Menu
from .forms import MenuForm
from applications.users.models import User
from applications.users.forms import UserRegisterForm

# Create your views here.

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "owner/index.html"
    login_url = reverse_lazy("users_app:user-login")

class ListUser(ListView):
    template_name = "owner/usuarios.html"
    model = User
    context_object_name = "usuario"

class ListMenu(ListView):
    template_name = "owner/menu.html"
    model = Menu
    context_object_name = "menu"
    
class UsersPage(TemplateView):
    template_name = "owner/usuarios.html"

class UserCreateView(FormView):
    template_name = "owner/crear-usuario.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("owner_app:lista-usuarios")

    def form_valid(self, form): 
        User.objects.create_user(
            form.cleaned_data["username"],
            form.cleaned_data["email"],
            form.cleaned_data["password1"],
            name = form.cleaned_data["name"],
            last_name = form.cleaned_data["last_name"],
            last_name_2 = form.cleaned_data["last_name_2"],
            rol = form.cleaned_data["rol"],
            phone_number = form.cleaned_data["phone_number"]
        )
        return super(UserCreateView, self).form_valid(form)

class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy("owner_app:panel-menu")

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = "owner/add-menu.html"  # Template para renderizar en el modal
    success_url = reverse_lazy("owner_app:panel-menu")

class MenuUpdateView(UpdateView):
    model = Menu
    fields = ["nombre", "descripcion"]
    template_name = "owner/update-menu.html"
    success_url = reverse_lazy("owner_app:panel-menu")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            # Renderiza el formulario como HTML y lo devuelve en un JSON
            html = render_to_string(self.template_name, {"form": form})
            return JsonResponse({"html": html, "success": True})
        return response
