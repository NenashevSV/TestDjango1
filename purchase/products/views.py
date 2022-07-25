from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm

class ProductsList(ListView):
	model = Product
	template_name = 'products/list.html'
	context_object_name = 'Products'
	paginate_by = 3


class CreateProduct(CreateView):
	form_class = ProductForm
	template_name = 'products/create.html'


class ViewProduct(DetailView):
	model = Product
	template_name = 'products/view.html'
	context_object_name = 'Product'
#	pk_url_kwarg = 'Product_id'

class EditProduct(UpdateView):
	model = Product
	form_class = ProductForm
	template_name = 'products/edit.html'
	context_object_name = 'Product'

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['photoURL'] = self.object.photo.url
	# 	return context


class DeleteProduct(DeleteView):
	model = Product
	success_url = reverse_lazy('ProductsList')
	template_name = 'products/delete.html'