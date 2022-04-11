from django import forms


class SignInForm(forms.Form):

    login = forms.CharField()
    password = forms.CharField(widget=forms.widgets.PasswordInput())

    error_css_class = 'error'  # TODO чек документацию нужно это и можно ли использовать
