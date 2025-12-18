from django import forms
from .models import CertificateExpiry, CertificateUser

class CertificateExpiryForm(forms.ModelForm):
    class Meta:
        model = CertificateExpiry
        fields = ['full_name', 'department', 'expiry_date']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CertificateUserForm(forms.ModelForm):
    class Meta:
        model = CertificateUser
        fields = ['full_name', 'computer_number', 'installed_certificate']

# Новые формы для фильтров
class CertificateExpiryFilterForm(forms.Form):
    full_name = forms.CharField(required=False, label="ФИО", widget=forms.TextInput(attrs={'placeholder': 'Поиск по ФИО'}))
    department = forms.CharField(required=False, label="ОТДЕЛ", widget=forms.TextInput(attrs={'placeholder': 'Поиск по отделу'}))
    expiry_date_from = forms.DateField(required=False, label="Дата начала", widget=forms.DateInput(attrs={'type': 'date'}))
    expiry_date_to = forms.DateField(required=False, label="Дата окончания", widget=forms.DateInput(attrs={'type': 'date'}))

class CertificateUserFilterForm(forms.Form):
    full_name = forms.CharField(required=False, label="ФИО", widget=forms.TextInput(attrs={'placeholder': 'Поиск по ФИО'}))
    computer_number = forms.CharField(required=False, label="Номер компьютера", widget=forms.TextInput(attrs={'placeholder': 'Поиск по номеру'}))
    installed_certificate = forms.CharField(required=False, label="Сертификат", widget=forms.TextInput(attrs={'placeholder': 'Поиск по сертификату'}))