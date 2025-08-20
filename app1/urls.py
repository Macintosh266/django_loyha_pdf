from django.urls import path
from .views import *

urlpatterns=[
    path('',Menu,name='home'),
    path('create_car/',CreateCar.as_view(),name='create_car'),
    path('create_carmodel/',CreateCarModel.as_view(),name='create_carmodel'),
    path('update_car/<int:pk>/',UpdateCar.as_view(),name='update_car'),
    path('detail_car/<int:pk>/',DetailCar.as_view(), name='detail_car'),
    path('delete_car/<int:pk>/', DeleteCar, name='delete_car'),
    path('pdf_download/<int:pk>/', PdfDownload, name='pdf_download'),
]