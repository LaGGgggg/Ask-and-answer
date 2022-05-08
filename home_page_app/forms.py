from django import forms


class MakeQuestionForm(forms.Form):

    title = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'input'}),
        min_length=10,
        max_length=30,
    )
    content = forms.CharField(
        widget=forms.widgets.Textarea(attrs={'class': 'input_big'}),
        min_length=160,
    )


class MakeCommentForm(forms.Form):

    content = forms.CharField(
        widget=forms.widgets.Textarea(attrs={'class': 'input'}),
    )


class SearchQuestionForm(forms.Form):

    content = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'input'}),
        max_length=50
    )
