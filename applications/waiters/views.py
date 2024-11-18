from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from applications.owner.models import Menu

# Create your views here.

class WaiterPage(LoginRequiredMixin, TemplateView):
    template_name = "waiter/mesas.html"
    login_url = reverse_lazy("users_app:user-login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mesas'] = range(1, 13)  
        return context

def ListaMenu(request, mesa):
    platillos = Menu.objects.all()
    return render(request, "waiter/index.html", {"platillos": platillos, "mesa": mesa})