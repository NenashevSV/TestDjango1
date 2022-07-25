from django import forms
from .models import Product

class NumberInput(forms.TextInput):
	input_type = 'number'


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'purchase_price', 'sale_price']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'purchase_price': NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
			'sale_price': NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
		}