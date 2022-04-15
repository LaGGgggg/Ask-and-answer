from django import forms


class SignInForm(forms.Form):

    login = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'default-input'}), max_length=20)
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'default-input'}), max_length=20)


class SignUpForm(forms.Form):

    login = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'default-input'}), max_length=20)
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'default-input'}), max_length=20)
    password_confirm = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class': 'default-input'}),
                                       max_length=20)
