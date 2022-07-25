from django.urls import path
from .views import *

urlpatterns = [
    path('', CustomersList.as_view(), name='CustomersList'),
    path('create/', CreateCustomer.as_view(), name='CreateCustomer'),
    path('edit/<int:pk>', EditCustomer.as_view(), name='EditCustomer'),
    path('view/<int:pk>', ViewCustomer.as_view(), name='ViewCustomer'),
    path('delete/<int:pk>', DeleteCustomer.as_view(), name='DeleteCustomer'),
]
