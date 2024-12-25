from django.contrib import admin
from .models import User

# User modelini admin arayüzüne kaydetme
admin.site.register(User)

# Daha fazla özelleştirme için ModelAdmin sınıfını kullanabilirsiniz
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Özelleştirilmiş ModelAdmin ile User modelini kaydetme
admin.site.unregister(User)
admin.site.register(User, UserAdmin)