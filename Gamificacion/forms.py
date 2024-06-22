from django import forms

class RegistrationForm(forms.Form):
    avatar = forms.ChoiceField(choices=[('bob', 'Bob'), ('alice', 'Alice')])
    userName = forms.CharField(max_length=100)
