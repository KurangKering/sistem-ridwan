from django.urls import path
from .datatables_view import *

from . import views

urlpatterns = [
    path('data-latih/', views.data_latih_index, name='pemain_belakang/data-latih/index'),
    path('data-latih/insert', views.data_latih_insert, name='pemain_belakang/data-latih/insert'),
    path('data-latih/create_or_update', views.data_latih_create_or_update, name='pemain_belakang/data-latih/create_or_update'),
    path('data-latih/update', views.data_latih_update, name='pemain_belakang/data-latih/update'),
    path('data-latih/delete', views.data_latih_delete, name='pemain_belakang/data-latih/delete'),
    path('data-latih/detail', views.data_latih_detail, name='pemain_belakang/data-latih/detail'),
    path('data-latih/datatables', DataLatihPemainBelakangDataTables.as_view(), name='pemain_belakang/data-latih/datatables'),
    path('data-latih/import', views.data_latih_import, name='pemain_belakang/data-latih/import'),
    path('pengujian/', views.pengujian_index, name='pemain_belakang/pengujian/index'),
    path('pengujian/proses', views.pengujian_proses, name='pemain_belakang/pengujian/proses'),
]
