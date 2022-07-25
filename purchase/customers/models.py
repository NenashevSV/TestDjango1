from django.db import models
from django.urls import reverse

class Customer (models.Model):
	MAN = 'm'
	WOMAN = 'w'
	NONE = ''
	GENDER_CHOICES = [
		(NONE, ''),
		(MAN, 'мужской'),
		(WOMAN, 'женский')
	]
	FIO = models.CharField(max_length=200, verbose_name="ФИО")
	birthDate = models.DateField(verbose_name='Дата рождения')
	registerDate = models.DateField(auto_now=True, verbose_name='Дата регистрации')
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None, verbose_name='Пол')
	PDConsent = models.BooleanField(default=False, verbose_name='Согласие на обработку ПД')
	photo = models.ImageField(upload_to='CustomersPhotos/%Y/%m/%d/', verbose_name='Фотография', blank=True)

	class Meta:
		ordering = ['FIO', 'birthDate', 'registerDate']
		verbose_name = 'Покупатель (я)'
		verbose_name_plural = 'Покупатели'


	def __str__(self):
		return f"{self.FIO} - {self.birthDate}"


	def get_absolute_url(self):
		return reverse('ViewCustomer', kwargs={'pk': self.pk})
