from django.db import models
from django.urls import reverse

class Product (models.Model):
	name = models.CharField(max_length=200, unique=True, verbose_name="Наименование")
	purchase_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена покупки")
	sale_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена продажи")

	class Meta:
		ordering = ['name']
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'


	def __str__(self):
		return f"{self.name} - {self.sale_price}"


	def get_absolute_url(self):
		return reverse('ViewProduct', kwargs={'pk': self.pk})
