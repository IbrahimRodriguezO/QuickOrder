from urllib import request
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView
from .models import Menu
from .forms import MenuForm

# Create your views here.

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "owner/index.html"
    login_url = reverse_lazy("users_app:user-login")

class ListMenu(ListView):
    template_name = "owner/menu.html"
    model = Menu
    context_object_name = "menu"
    

class UsersPage(TemplateView):
    template_name = "owner/usuarios.html"

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
