from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from .forms import ProductForm

class ProductListView(View):
    """Tüm ürünleri listeleme görünümü."""
    def get(self, request):
        products = Product.objects.filter(available=True)  # Sadece mevcut ürünleri al
        return render(request, 'products/product_list.html', {'products': products})

class ProductDetailView(View):
    """Belirli bir ürünün detaylarını görüntüleme görünümü."""
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)  # Ürünü slug ile al
        return render(request, 'products/product_detail.html', {'product': product})

class ProductCreateView(View):
    """Yeni bir ürün oluşturma görünümü."""
    def get(self, request):
        form = ProductForm()
        return render(request, 'products/product_form.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Ürün listesine yönlendir
        return render(request, 'products/product_form.html', {'form': form})

class ProductUpdateView(View):
    """Mevcut bir ürünü güncelleme görünümü."""
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = ProductForm(instance=product)
        return render(request, 'products/product_form.html', {'form': form})

    def post(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Ürün listesine yönlendir
        return render(request, 'products/product_form.html', {'form': form})