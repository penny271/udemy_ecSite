from django.urls import path
from .views import (
    ProductListView, Product_DetailView,
)

app_name='stores'

urlpatterns = [
    path('product_list', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', ProductListView.as_view(), name='product_detail'),
]
