from django import forms


class SignInForm(forms.Form):

    login = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'default-input'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'default-input'}))


class SignUpForm(forms.Form):

    login = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'default-input'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'default-input'}))
    password_confirm = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'default-input'}))
