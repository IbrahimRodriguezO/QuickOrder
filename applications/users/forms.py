from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña"
            }
        )
    )

    password2 = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repetir contraseña"
            }
        )
    )

    class Meta:

        model = User
        fields = (
            'name',
            'last_name',
            'last_name_2',
            'rol',
            'phone_number',
            'username',
            'email',
        )

    def clean_password2(self):
        if (self.cleaned_data["password1"] != self.cleaned_data["password2"]):
            self.add_error("password2", "Las contraseñas no son las mismas")

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuario",
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'input'}
        )
    )
    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Los datos del usuario no son correctos")
        
        return cleaned_data