from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.sitemaps import *
from django.contrib.sitemaps.views import sitemap
sitemaps = {
    'static': StaticViewSitemap,
    'services': ServicesSitemap,
    'blog': BlogSitemap
}
admin.site.site_header = "KOSMOS"
admin.site.site_title = "KOSMOS администрирование"
admin.site.index_title = "KOSMOS администрирование"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('', include('pages.urls')),
    path('callback/', include('callback.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)