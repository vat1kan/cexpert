from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from Cars.views import error_404, traceback_handler

handler404 = error_404
handler500 = traceback_handler
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('Cars.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
