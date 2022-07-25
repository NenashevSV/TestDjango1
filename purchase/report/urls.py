from django.urls import path
from .views import *

urlpatterns = [
    path('', ReportList.as_view(), name='ReportList'),
]
