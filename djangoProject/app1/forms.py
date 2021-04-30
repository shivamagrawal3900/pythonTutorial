from django import forms

from app1.models import User


class UserForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput, max_length=50)
    email = forms.EmailField(required=True, widget=forms.EmailInput, max_length=50)
    phone = forms.CharField(required=True, widget=forms.TextInput)
    dob = forms.DateField(required=True, widget=forms.DateInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'dob']
