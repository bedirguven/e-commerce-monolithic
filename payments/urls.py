from django.urls import path
from .views import PaymentListView, PaymentDetailView, PaymentCreateView

urlpatterns = [
    path('', PaymentListView.as_view(), name='payment_list'),
    path('<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
    path('create/', PaymentCreateView.as_view(), name='payment_create'),
]