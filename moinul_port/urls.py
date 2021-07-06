from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from django_otp.admin import OTPAdminSite
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('nill/antu/ad/', admin.site.urls),
    path('',include('antu.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Nill Port Test'
admin.site.site_title = 'Nill Port Test'