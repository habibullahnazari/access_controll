from .views import *
from django.urls import path

urlpatterns = [
    # path('',home)
    path('', index),
    path('searchpage', searchpage),
    path('qr', indexqr),


]
