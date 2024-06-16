from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 
                  'first_name', 
                  'last_name', 
                  'rut', 
                  'gender', 
                  'password1', 
                  'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")


class StaffUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[
        ('SELLER', 'Vendedor'),
        ('WAREHOUSE', 'Bodeguero'),
        ('ACCOUNTANT', 'Contador'),
    ])

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'rut', 'gender', 'role', 'password1', 'password2')

