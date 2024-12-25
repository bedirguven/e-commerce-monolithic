from django.contrib import admin
from django.urls import path, include
from .views import home_view,about_view,contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
]

# Opsiyonel olarak, hata sayfalarınızı özelleştirebilirsiniz
from django.conf.urls import handler404, handler500
from .views import my_custom_404_view, my_custom_500_view

handler404 = 'my_custom_404_view'
handler500 = 'my_custom_500_view'