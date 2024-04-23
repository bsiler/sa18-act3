from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_index, name='product_index'),
]
