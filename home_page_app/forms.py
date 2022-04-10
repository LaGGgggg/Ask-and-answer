from django import forms


class SignInForm(forms.Form):

    login = forms.CharField()
    password = forms.CharField(widget=forms.widgets.PasswordInput())
