from django.db import models
from django.urls import reverse
from customers.models import Customer
from products.models import Product

class Registry (models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name="Покупатель")
	sale_date = models.DateField(verbose_name="Дата продажи")

	class Meta:
		ordering = ['-sale_date', 'customer']
		verbose_name = 'Реестр'
		verbose_name_plural = 'Реестр'


	def __str__(self):
		return f"{self.customer}-{self.sale_date}"


	def get_absolute_url(self):
		return reverse('ViewRegistry', kwargs={'pk': self.pk})


class RegistryData (models.Model):
	registry = models.ForeignKey(Registry, on_delete=models.PROTECT, verbose_name="Строка реестра")
	product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Товар")
	count = models.IntegerField(verbose_name='Кол-во')
	price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена за единицу", blank=True, null=True)
	sum = models.DecimalField(max_digits=22, decimal_places=2, verbose_name="Сумма", blank=True, null=True)

	class Meta:
		ordering = ['-registry', 'sum']
		verbose_name = 'Данные покупок'
		verbose_name_plural = 'Данные покупок'

	def __str__(self):
		return f"{self.registry}-{self.product}"

	def get_absolute_url(self):
		return reverse('ViewRegistry', kwargs={'pk': self.pk})
