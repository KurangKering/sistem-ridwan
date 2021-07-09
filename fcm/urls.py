from django.urls import path

from . import views

urlpatterns = [
    path('data-latih/', views.index_data_latih, name="data-latih/index"),
]
