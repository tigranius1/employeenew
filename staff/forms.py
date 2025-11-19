# staff/forms.py
from django import forms

class EmployeeForm(forms.Form):
    tab_number = forms.CharField(
        label='Табельный номер',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    full_name = forms.CharField(
        label='ФИО',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    position = forms.CharField(
        label='Должность',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )