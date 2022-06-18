from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class RegistrationFrom(UserCreationForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            auth_user = authenticate(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password1']
            )
            login(self.request, auth_user)

        return user

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
