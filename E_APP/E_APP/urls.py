
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import accounts.urls
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/',include(accounts.urls))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
