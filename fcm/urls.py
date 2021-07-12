from django.urls import path
from .datatables_view import *

from . import views

urlpatterns = [
    path('data-latih-kiper/', views.index_data_latih_kiper, name="data-latih-kiper/index"),
    path('data-latih-kiper/insert', views.insert_data_latih_kiper, name="data-latih-kiper/insert"),
    path('data-latih-kiper/create_or_update', views.create_or_update_data_latih_kiper, name="data-latih-kiper/create_or_update"),
    path('data-latih-kiper/update', views.update_data_latih_kiper, name="data-latih-kiper/update"),
    path('data-latih-kiper/delete', views.delete_data_latih_kiper, name="data-latih-kiper/delete"),
    path('data-latih-kiper/detail', views.detail_data_latih_kiper, name="data-latih-kiper/detail"),
    path('data-latih-kiper/show_all', DataLatihKiperDataTables.as_view(), name="data-latih-kiper/show_all"),
    path('data-latih-kiper/import', views.import_data_latih_kiper, name="data-latih-kiper/import"),
    path('pengujian/kiper', views.index_pengujian_kiper, name="pengujian/kiper"),
    path('pengujian/proses_pengujian_kiper', views.proses_pengujian_kiper, name="pengujian/proses_pengujian_kiper"),
]
