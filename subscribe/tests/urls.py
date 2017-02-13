"""
This ``urls.py`` is only used when running the tests via ``runtests.py``.
As you know, every app must be hooked into yout main ``urls.py`` so that
you can actually reach the app's views (provided it has any views, of course).

"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^', include('subscribe.urls')),
]
