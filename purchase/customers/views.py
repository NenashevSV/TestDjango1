from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm

class CustomersList(ListView):
	model = Customer
	template_name = 'customers/list.html'
	context_object_name = 'customers'
	paginate_by = 3


class CreateCustomer(CreateView):
	form_class = CustomerForm
	template_name = 'customers/create.html'


class ViewCustomer(DetailView):
	model = Customer
	template_name = 'customers/view.html'
	context_object_name = 'customer'
#	pk_url_kwarg = 'customer_id'

class EditCustomer(UpdateView):
	model = Customer
	form_class = CustomerForm
	template_name = 'customers/edit.html'
	context_object_name = 'customer'

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['photoURL'] = self.object.photo.url
	# 	return context


class DeleteCustomer(DeleteView):
	model = Customer
	success_url = reverse_lazy('CustomersList')
	template_name = 'customers/delete.html'