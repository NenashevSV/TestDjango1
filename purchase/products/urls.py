from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductsList.as_view(), name='ProductsList'),
    path('create/', CreateProduct.as_view(), name='CreateProduct'),
    path('edit/<int:pk>', EditProduct.as_view(), name='EditProduct'),
    path('view/<int:pk>', ViewProduct.as_view(), name='ViewProduct'),
    path('delete/<int:pk>', DeleteProduct.as_view(), name='DeleteProduct'),
]
