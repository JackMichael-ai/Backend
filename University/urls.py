from django.conf.urls.static import static
from django.conf import settings # Standard import pattern
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # We REMOVED the auth_views and accounts lines.
    # Now, EVERYTHING that isn't 'admin/' goes to your Admin app.
    path('', include('Admin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)