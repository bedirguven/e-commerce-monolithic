from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Product
from .models import Order, OrderItem
from django.urls import reverse

class OrderModelTest(TestCase):
    def setUp(self):
        # Kullanıcı ve ürün oluşturma
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
        # Sipariş oluşturma
        self.order = Order.objects.create(
            customer=self.user,
            shipping_address="123 Test Street",
            billing_address="123 Test Street",
            status="Pending"
        )
        # Sipariş öğesi ekleme
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            price=self.product.price
        )

    def test_order_creation(self):
        """Siparişin doğru bir şekilde oluşturulduğunu test eder."""
        self.assertEqual(self.order.customer, self.user)
        self.assertEqual(self.order.status, "Pending")
        self.assertEqual(self.order.items.count(), 1)

    def test_order_item_total_price(self):
        """Sipariş öğesinin toplam fiyatını test eder."""
        total_price = self.order_item.get_total_price()
        self.assertEqual(total_price, 100.00)  # 2 x 50.00

class OrderViewsTest(TestCase):
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

    def test_order_list_view(self):
        """Sipariş listeleme görünümünün çalıştığını test eder."""
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.id)
        self.assertTemplateUsed(response, 'orders/order_list.html')

    def test_order_detail_view(self):
        """Sipariş detay görünümünün çalıştığını test eder."""
        response = self.client.get(reverse('order_detail', args=[self.order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.shipping_address)
        self.assertTemplateUsed(response, 'orders/order_detail.html')

    def test_order_create_view(self):
        """Sipariş oluşturma görünümünün çalıştığını test eder."""
        response = self.client.post(reverse('order_create'), {
            'shipping_address': "456 New Street",
            'billing_address': "456 New Street",
            'status': "Pending"
        })
        self.assertEqual(response.status_code, 302)  # Başarılı yönlendirme
        self.assertEqual(Order.objects.count(), 2)  # Yeni sipariş oluşturuldu