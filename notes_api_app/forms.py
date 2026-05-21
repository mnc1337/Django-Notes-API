"""
Forms configuration
"""

from django import forms
from django.contrib.auth.models import User
from .models import Note


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")
        widgets = {
            "password": forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "content", "is_important")
