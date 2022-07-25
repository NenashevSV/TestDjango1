from django import forms
from .models import Customer

class DropDateInput(forms.TextInput):
	input_type = 'date'

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['FIO', 'birthDate', 'gender', 'PDConsent', 'photo']
		widgets = {
			'FIO': forms.TextInput(attrs={'class': 'form-control'}),
			'birthDate': DropDateInput(attrs={'class': 'form-control'}),
			'gender': forms.Select(attrs={'class': 'form-control', 'type': 'date'}),
		}