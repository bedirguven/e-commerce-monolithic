from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    """
    Ana sayfa görünümü.
    """
    return render(request, 'ecommerce/htmls/home.html')

def about_view(request):
    """
    Hakkında sayfası görünümü.
    """
    return render(request, 'ecommerce/htmls/about.html')

def contact_view(request):
    """
    İletişim sayfası görünümü.
    """
    return render(request, 'ecommerce/htmls/contact.html')

def my_custom_404_view(request, exception):
    """
    Özel 404 hata sayfası görünümü.
    """
    return render(request, 'ecommerce/htmls/404.html', status=404)

def my_custom_500_view(request):
    """
    Özel 500 hata sayfası görünümü.
    """
    return render(request, 'ecommerce/htmls/500.html', status=500)