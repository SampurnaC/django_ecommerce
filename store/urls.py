from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>', views.product_show, name='product_show'),
    path('category/<str:cat>', views.category_products, name='category_products')
    
]
