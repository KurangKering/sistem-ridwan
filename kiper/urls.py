from django.urls import path
from .datatables_view import *

from . import views

urlpatterns = [
    path('data-latih/', views.data_latih_index, name='kiper/data-latih/index'),
    path('data-latih/insert', views.data_latih_insert, name='kiper/data-latih/insert'),
    path('data-latih/create_or_update', views.data_latih_create_or_update, name='kiper/data-latih/create_or_update'),
    path('data-latih/update', views.data_latih_update, name='kiper/data-latih/update'),
    path('data-latih/delete', views.data_latih_delete, name='kiper/data-latih/delete'),
    path('data-latih/detail', views.data_latih_detail, name='kiper/data-latih/detail'),
    path('data-latih/datatables', DataLatihKiperDataTables.as_view(), name='kiper/data-latih/datatables'),
    path('data-latih/import', views.data_latih_import, name='kiper/data-latih/import'),
    path('pengujian/', views.pengujian_index, name='kiper/pengujian/index'),
    path('pengujian/proses', views.pengujian_proses, name='kiper/pengujian/proses'),
]
