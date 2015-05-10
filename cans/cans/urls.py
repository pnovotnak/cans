from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from ui import urls as ui_urls

from settings import DEBUG, MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(ui_urls, namespace='ui')),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


