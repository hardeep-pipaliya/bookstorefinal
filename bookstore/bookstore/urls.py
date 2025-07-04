from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('books.urls')),
    path("", include("django.contrib.auth.urls")),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

