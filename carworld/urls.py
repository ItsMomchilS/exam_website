from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('carworld.common.urls')),
                  path('vehicles/', include('carworld.vehicles.urls')),
                  path('accounts/', include('carworld.accounts.urls')),
                  path('others/', include('carworld.others.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
