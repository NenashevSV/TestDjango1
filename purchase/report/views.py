import datetime

from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from customers.models import Customer
from registrys.models import Registry, RegistryData
from products.models import Product

class ReportList(ListView):
	template_name = 'report/list.html'
	context_object_name = 'report'
	paginate_by = 20

	def get_queryset(self):
		query = '''
			select g.id, cc.FIO, g.itogo from customers_customer as cc
			inner join 
				(select c.id, sum(rr.sum) itogo from customers_customer as c
				left join registrys_registry as r on c.id=r.customer_id and r.sale_date = %s
				left join registrys_registrydata as rr on r.id=rr.registry_id
				group by c.id) g on cc.id=g.id
			order by g.itogo desc
		'''
		Date = self.request.GET.get('Date', False)
		if Date:
			Date = self.request.GET['Date']
		else:
			Date = datetime.date.today().strftime("%Y-%m-%d")
		queryset = Customer.objects.raw(query, [Date])
		return queryset


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		dt = context['view'].request.GET.get('Date', False)
		if dt:
			context['Date'] = datetime.datetime.strptime(self.request.GET['Date'],'%Y-%m-%d')
		else:
			context['Date'] = datetime.date.today()#.strftime("%Y-%m-%d")
		return context

