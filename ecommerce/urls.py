
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

#Here just definer a patterns for the image and then call the image field in the template
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)