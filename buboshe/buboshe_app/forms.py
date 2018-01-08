"""
    Author: junxuan
    Date: 2017-12-26
"""
from django import forms
from buboshe_app.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
           "nickname", "email",
        )
