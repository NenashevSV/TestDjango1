from django import forms
from .models import Registry, RegistryData

class NumberInput(forms.TextInput):
	input_type = 'number'

class DropDateInput(forms.TextInput):
	input_type = 'date'

class RegistryForm(forms.ModelForm):
	class Meta:
		model = Registry
		fields = ['customer', 'sale_date']
		widgets = {
			'customer': forms.Select(attrs={'class': 'form-control'}),
			'sale_date': DropDateInput(attrs={'class': 'form-control'}),
		}


class RegistryDataFormCreate(forms.ModelForm):
	class Meta:
		model = RegistryData
		fields = ['product', 'count']
		widgets = {
			'product': forms.Select(attrs={'class': 'form-control'}),
			'count': NumberInput(attrs={'class': 'form-control'}),
		}


class RegistryDataFormView(forms.ModelForm):
	class Meta:
		model = RegistryData
		fields = ['registry', 'product', 'count', 'price', 'sum']
		widgets = {
			'registry': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly', 'disable': 'disable'}),
			'product': forms.Select(attrs={'class': 'form-control'}),
			'count': NumberInput(attrs={'class': 'form-control'}),
			'price': NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'readonly': 'readonly'}),
			'sum': NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'readonly': 'readonly'}),
		}
