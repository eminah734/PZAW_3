from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(username=email).exists():
            raise ValidationError("Użytkownik o tym emailu już istnieje!")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password"])
        
        if commit:
            user.save()
        return user