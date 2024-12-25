from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Payment
from .forms import PaymentForm

@method_decorator(login_required, name='dispatch')
class PaymentListView(View):
    """Kullanıcının ödemelerini listeleme."""
    def get(self, request):
        payments = Payment.objects.filter(customer=request.user).order_by('-created_at')
        return render(request, 'payments/payment_list.html', {'payments': payments})

@method_decorator(login_required, name='dispatch')
class PaymentDetailView(View):
    """Belirli bir ödemenin detaylarını görüntüleme."""
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk, customer=request.user)
        return render(request, 'payments/payment_detail.html', {'payment': payment})

@method_decorator(login_required, name='dispatch')
class PaymentCreateView(View):
    """Yeni bir ödeme oluşturma."""
    def get(self, request):
        form = PaymentForm()
        return render(request, 'payments/payment_form.html', {'form': form})

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.customer = request.user  # Ödemeye giriş yapmış kullanıcıyı atayın
            payment.save()
            return redirect('payment_list')  # Ödeme listesine yönlendirin
        return render(request, 'payments/payment_form.html', {'form': form})