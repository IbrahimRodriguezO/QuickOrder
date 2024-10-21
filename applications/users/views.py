from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, LoginForm
from .models import User

# Create your views here.
class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = "/"
    
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
        return super(UserRegisterView, self).form_valid(form)
    
class LoginUser(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    # success_url = reverse_lazy("owner_app:panel")
    def get_success_url(self):
        user = self.request.user
        # Redirige a los paneles según el rol del usuario
        if user.rol == 'owner':
            return reverse_lazy('owner_app:panel')
        elif user.rol == 'waiter':
            return reverse_lazy('waiter_app:panel-waiter')
        elif user.rol == 'chef':
            return reverse_lazy('chef_app:panel-chef')
        else:
            return reverse_lazy('users:login')  # O redirig

    def form_valid(self, form): 
        user = authenticate(
            username = form.cleaned_data["username"],
            password = form.cleaned_data["password"]
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)
    
class LogoutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )