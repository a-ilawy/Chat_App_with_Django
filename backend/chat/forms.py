from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Room

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["room_name"]
        widgets = {
            "room_name": forms.TextInput(attrs={"placeholder": "Enter new room name"})
        }
