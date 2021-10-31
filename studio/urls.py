from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),

    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),

    path('', include('main_page.urls')),
    path('smm-prodvijenie/', include('smm.urls')),
    path('kontakty/', include('contacts.urls')),
    path('web-razrabotka/', include('webdev.urls')),
    path('seo-prodvijenie/', include('seo.urls')),
    path('logotip/', include('logo_and_style.urls')),
    path('contextnaya-reklama/', include('contextadv.urls')),
    path('marketingovaya-strategiya/', include('marketing_strategy.urls')),
    path('brendbook/', include('brandbook.urls')),
    path('target-reklama/', include('target.urls')),
    path('keysi/', include('cases.urls')),
    path('keysi/<slug:category_slug>', include('cases.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
