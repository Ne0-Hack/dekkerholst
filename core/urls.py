from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "DEKKERHOLST: Панель администрирования"
admin.site.site_title = "DEKKERHOLST: Панель администрирования"
admin.site.index_title = "Главная"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WWW.urls')),
    path('callbacks/', include('callbacks.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
