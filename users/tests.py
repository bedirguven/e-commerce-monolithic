from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTestCase(TestCase):
    def setUp(self):
        """Test öncesinde bir kullanıcı oluştur."""
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )

    def test_user_creation(self):
        """Kullanıcı oluşturma testi."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(isinstance(self.user, self.User))
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_user_email(self):
        """Kullanıcı e-posta adresinin doğruluğunu test et."""
        self.assertEqual(self.user.email, 'test@example.com')

    def test_user_password(self):
        """Kullanıcı şifresinin doğru set edilip edilmediğini kontrol et."""
        # Kullanıcı şifresinin çıktığını doğrudan kontrol etmek mümkün değildir,
        # bunun yerine şifrenin doğrulanması sağlanmalıdır.
        self.assertTrue(self.user.check_password('password123'))