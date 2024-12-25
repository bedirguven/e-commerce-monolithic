from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Order, OrderItem
from .forms import OrderCreateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class OrderListView(View):
    """Kullanıcının siparişlerini listeleme."""
    def get(self, request):
        orders = Order.objects.filter(customer=request.user).order_by('-created_at')
        return render(request, 'orders/order_list.html', {'orders': orders})

@method_decorator(login_required, name='dispatch')
class OrderDetailView(View):
    """Belirli bir siparişin detaylarını görüntüleme."""
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk, customer=request.user)
        return render(request, 'orders/order_detail.html', {'order': order})

@method_decorator(login_required, name='dispatch')
class OrderCreateView(View):
    """Yeni bir sipariş oluşturma."""
    def get(self, request):
        form = OrderCreateForm()
        return render(request, 'orders/order_form.html', {'form': form})

    def post(self, request):
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user  # Siparişe giriş yapmış kullanıcıyı atayın
            order.save()
            # Sipariş öğelerini ekleyin (örnek)
            for item in request.session.get('cart', []):
                OrderItem.objects.create(
                    order=order,
                    product_id=item['product_id'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            return redirect('order_list')  # Sipariş listesine yönlendirin
        return render(request, 'orders/order_form.html', {'form': form})