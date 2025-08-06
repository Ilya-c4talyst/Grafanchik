from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Подключаем URL нашего приложения
    path('', include('django_prometheus.urls')),  # Это должно быть здесь!
]