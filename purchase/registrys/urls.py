from django.urls import path
from .views import *

urlpatterns = [
    path('', RegistryList.as_view(), name='RegistrysList'),
    path('create/', CreateRegistry.as_view(), name='CreateRegistry'),
    path('edit/<int:pk>', EditRegistry.as_view(), name='EditRegistry'),
    path('view/<int:pk>', ViewRegistry.as_view(), name='ViewRegistry'),
    path('delete/<int:pk>', DeleteRegistry.as_view(), name='DeleteRegistry'),
    # path('data/', RegistryDataList.as_view(), name='RegistryDataList'),
    path('data/create/<int:pk>', CreateRegistryData, name='CreateRegistryData'),
    path('data/edit/<int:pk>', EditRegistryData.as_view(), name='EditRegistryData'),
    path('data/delete/<int:pk>', DeleteRegistryData.as_view(), name='DeleteRegistryData'),

]
