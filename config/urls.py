from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from config.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
]
urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
