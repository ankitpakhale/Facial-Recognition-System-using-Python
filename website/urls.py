from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('', views.login_redirect),
    url('admin/', admin.site.urls),
    url('home/', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
