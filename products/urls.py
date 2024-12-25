from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', ProductCreateView.as_view(), name='product_add'),
    path('<slug:slug>/edit/', ProductUpdateView.as_view(), name='product_edit'),
]