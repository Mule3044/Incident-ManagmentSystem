from django.contrib.auth.models import User
from django import forms
from .models import FieldOfficer, FieldOfficerDispatch


class FieldOfficerForm(forms.ModelForm):

    class Meta:
        model = FieldOfficer
        fields = ['firstName', 'lastName', 'phoneNumber', 'policeStation' ,'status']


class FieldOfficerDispatchForm(forms.ModelForm):

    class Meta:
        model = FieldOfficerDispatch
        fields = ['fieldOfficer','dispatchedDate', 'policeStallName']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']