from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from orders.models import Order
from products.models import Product
from .models import Payment

class PaymentModelTest(TestCase):
    def setUp(self):
        # Kullanıcı, ürün ve sipariş oluşturma
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpass'
        )
        self.product = Product.objects.create(
            name="Test Product",
            description="A test product.",
            price=50.00,
            stock=10,
            available=True,
            slug="test-product"
        )
        self.order = Order.objects.create(
            customer=self.user,
            shipping_address="123 Test Street",
            billing_address="123 Test Street",
            status="Pending"
        )
        # Ödeme oluşturma
        self.payment = Payment.objects.create(
            customer=self.user,
            order=self.order,
            amount=100.00,
            payment_method="Credit Card",
            status="Completed",
            transaction_id="TRX12345"
        )

    def test_payment_creation(self):
        """Ödemenin doğru bir şekilde oluşturulduğunu test eder."""
        self.assertEqual(self.payment.customer, self.user)
        self.assertEqual(self.payment.order, self.order)
        self.assertEqual(self.payment.amount, 100.00)
        self.assertEqual(self.payment.status, "Completed")
        self.assertEqual(self.payment.transaction_id, "TRX12345")

    def test_payment_str_representation(self):
        """Ödemenin __str__ metodunu test eder."""
        self.assertEqual(str(self.payment), f"Payment {self.payment.id} - Completed")


class PaymentViewsTest(TestCase):
    def setUp(self):
        # Kullanıcı ve sipariş oluşturma
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpass'
        )
        self.client.login(username='testuser', password='testpass')

        self.order = Order.objects.create(
            customer=self.user,
            shipping_address="123 Test Street",
            billing_address="123 Test Street",
            status="Pending"
        )
        self.payment = Payment.objects.create(
            customer=self.user,
            order=self.order,
            amount=100.00,
            payment_method="Credit Card",
            status="Completed",
            transaction_id="TRX12345"
        )

    def test_payment_list_view(self):
        """Ödeme listeleme görünümünün çalıştığını test eder."""
        response = self.client.get(reverse('payment_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.payment.transaction_id)
        self.assertTemplateUsed(response, 'payments/payment_list.html')

    def test_payment_detail_view(self):
        """Ödeme detay görünümünün çalıştığını test eder."""
        response = self.client.get(reverse('payment_detail', args=[self.payment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.payment.transaction_id)
        self.assertTemplateUsed(response, 'payments/payment_detail.html')

    def test_payment_create_view(self):
        """Yeni ödeme oluşturma görünümünün çalıştığını test eder."""
        response = self.client.post(reverse('payment_create'), {
            'order': self.order.id,
            'amount': 150.00,
            'payment_method': "PayPal",
        })
        self.assertEqual(response.status_code, 302)  # Başarılı yönlendirme
        self.assertEqual(Payment.objects.count(), 2)  # Yeni ödeme oluşturuldu