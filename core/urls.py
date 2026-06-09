
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inventory import views
from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('api/books/', views.api_books),
    path('api/books/<int:pk>/', views.api_book_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)