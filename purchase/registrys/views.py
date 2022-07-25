from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Registry, RegistryData
from .forms import RegistryForm, RegistryDataFormCreate


class RegistryList(ListView):
	model = Registry
	template_name = 'registrys/list.html'
	context_object_name = 'Registrys'
	paginate_by = 3


class CreateRegistry(CreateView):
	form_class = RegistryForm
	template_name = 'registrys/create.html'


class ViewRegistry(DetailView):
	model = Registry
	template_name = 'registrys/view.html'
	context_object_name = 'Registry'
#	pk_url_kwarg = 'Product_id'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['RegistryData'] = RegistryData.objects.filter(registry=self.object)
		return context


class EditRegistry(UpdateView):
	model = Registry
	form_class = RegistryForm
	template_name = 'registrys/edit.html'
	context_object_name = 'Registry'

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['photoURL'] = self.object.photo.url
	# 	return context


class DeleteRegistry(DeleteView):
	model = Registry
	success_url = reverse_lazy('RegistryList')
	template_name = 'registrys/delete.html'


def CreateRegistryData(request, pk):
	registry_item = Registry.objects.get(pk=pk)
	if request.method == 'POST':
		form = RegistryDataFormCreate(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			data['registry'] = registry_item
			data['price'] = data['product'].sale_price
			data['sum'] = data['price'] * data['count']
			RegistryData.objects.create(**data)
			return redirect('ViewRegistry', pk)
	else:
		form = RegistryDataFormCreate
	return render(request, 'registrys/data/create.html', {'form': form, 'registry': registry_item})


class EditRegistryData(UpdateView):
	model = RegistryData
	form_class = RegistryDataFormCreate
	template_name = 'registrys/data/edit.html'
	context_object_name = 'RegistryData'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		pk = context['object'].pk
		registry_item = RegistryData.objects.get(pk=pk).registry
		context['registry'] = registry_item
		return context


class DeleteRegistryData(DeleteView):
	model = RegistryData
	template_name = 'registrys/data/delete.html'
	context_object_name = 'RegistryData'

	def get_success_url(self):
		pk = self.object.registry.pk
		return reverse_lazy('ViewRegistry', kwargs={'pk': pk})
