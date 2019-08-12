from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

handler500 = views.handler500

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('accounts/', include('apps.accounts.urls')),
    path('customers/', include('apps.customers.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:

    urlpatterns += [
        path('403/', TemplateView.as_view(template_name='403.html')),
        path('404/', TemplateView.as_view(template_name='404.html')),
        path('500/', TemplateView.as_view(template_name='500.html')),
        path('503/', TemplateView.as_view(template_name='503.html')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
