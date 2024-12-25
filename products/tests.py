from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product.",
            price=100.00,
            stock=10,
            available=True,
            category="Test Category",
            slug="test-product"
        )

    def test_product_creation(self):
        """Ürünün doğru bir şekilde oluşturulduğunu test et."""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100.00)
        self.assertTrue(self.product.available)

    def test_product_str_representation(self):
        """Ürünün __str__ metodunu test et."""
        self.assertEqual(str(self.product), "Test Product")

class ProductViewsTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product.",
            price=100.00,
            stock=10,
            available=True,
            category="Test Category",
            slug="test-product"
        )

    def test_product_list_view(self):
        """Ürün listeleme görünümünün çalıştığını test et."""
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertTemplateUsed(response, "products/product_list.html")

    def test_product_detail_view(self):
        """Ürün detay görünümünün çalıştığını test et."""
        response = self.client.get(reverse('product_detail', kwargs={'slug': self.product.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertTemplateUsed(response, "products/product_detail.html")

    def test_product_create_view(self):
        """Ürün oluşturma görünümünün çalıştığını test et."""
        response = self.client.post(reverse('product_add'), {
            'name': 'New Product',
            'description': 'A newly added product.',
            'price': 150.00,
            'stock': 20,
            'available': True,
            'category': 'New Category',
            'slug': 'new-product'
        })
        self.assertEqual(response.status_code, 302)  # Başarılı yönlendirme
        self.assertTrue(Product.objects.filter(name="New Product").exists())

    def test_product_update_view(self):
        """Ürün güncelleme görünümünün çalıştığını test et."""
        response = self.client.post(reverse('product_edit', kwargs={'slug': self.product.slug}), {
            'name': 'Updated Product',
            'description': 'Updated description.',
            'price': 200.00,
            'stock': 5,
            'available': False,
            'category': 'Updated Category',
            'slug': 'updated-product'
        })
        self.assertEqual(response.status_code, 302)  # Başarılı yönlendirme
        self.product.refresh_from_db()  # Veritabanından ürünü güncel durumu ile çek
        self.assertEqual(self.product.name, "Updated Product")
        self.assertEqual(self.product.price, 200.00)
        self.assertFalse(self.product.available)