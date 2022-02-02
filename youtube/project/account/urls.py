from django.urls import path
from .import  views

urlpatterns=[ path('register/',views.register, name='register'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     ]