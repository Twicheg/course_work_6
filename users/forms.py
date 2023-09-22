from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from clients.forms import StyleFormMixin
from users.models import User

#
# class UserForm(StyleFormMixin, UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('email', 'phone_number', 'country', 'password1', 'password2', 'avatar')
#
#
# class UserUpdateForm(StyleFormMixin, UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'phone_number', 'country', 'avatar')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['password'].widget = forms.HiddenInput()