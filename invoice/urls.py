from django.urls import path
from . import views

urlpatterns = [
     path('', views.create_invoice, name='home'),

     path('create_product/', views.create_product, name='create_product'),
     path('view_product/', views.view_product, name='view_product'),
     path('edit_product/<int:pk>', views.edit_product, name='edit_product'),
     path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
     path('upload_product_excel', views.upload_product_from_excel,
          name='upload_product_excel'),

     path('create_invoice/', views.create_invoice, name='create_invoice'),
     path('view_invoice/', views.view_invoice, name='view_invoice'),
     path('delete_invoice/<int:pk>/', views.delete_invoice, name='delete_invoice'),
     path('delete_all_invoice/', views.delete_all_invoice,
          name='delete_all_invoice'),
     path('download_all_invoice/', views.download_all,
          name='download_all_invoice'),
     path('view_invoice_detail/<int:pk>/',
          views.view_invoice_detail, name='view_invoice_detail'),
     path('genpdf/<int:pk>/', views.genpdf, name='genpdf'),
]
