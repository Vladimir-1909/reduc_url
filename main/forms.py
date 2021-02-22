from django import forms
from .models import LinkReduc


class LinkForm(forms.ModelForm):
    link = forms.CharField(
        label='Длинная ссылка',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ссылку'
        })
    )

    reducLink = forms.CharField(
        label='Сокращенная ссылка',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите слово сокращение'
        })
    )

    class Meta:
        model = LinkReduc
        fields = ['link', 'reducLink']