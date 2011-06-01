from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include('front.api_urls')),
    url(r'^', include('front.urls')),
)
