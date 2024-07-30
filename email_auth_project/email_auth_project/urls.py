
from django.contrib import admin
from django.urls import path
from auapp.views import ulogin, usignup, uhome, ulogout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", uhome, name = "uhome"),
    path("ulogin", ulogin, name = "ulogin"),
    path("usignup", usignup, name = "usignup"),
    path("ulogout", ulogout, name = "ulogout"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

