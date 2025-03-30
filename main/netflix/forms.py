from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    class Meta:
        mode = User
        fields = ['email','password']

    def save(self, commit = True) -> User:
        user = super().save(commit=True)
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user