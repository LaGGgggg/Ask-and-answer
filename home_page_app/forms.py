from django import forms


class SignInForm(forms.Form):

    login = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'input'}),
        min_length=5,
        max_length=20,
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'class': 'input'}),
        min_length=8,
        max_length=20,
    )


class SignUpForm(forms.Form):

    login = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'input'}),
        min_length=5,
        max_length=20,
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'class': 'input'}),
        min_length=8,
        max_length=20,
    )
    password_confirm = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'class': 'input'}),
        min_length=8,
        max_length=20,
    )


class MakeQuestionForm(forms.Form):

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input'}),
        min_length=10,
        max_length=30,
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'input_big'}),
        min_length=180,
    )
