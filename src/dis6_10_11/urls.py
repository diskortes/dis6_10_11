from django.conf.urls.defaults import patterns, include, url
from dis6_10_11.views import hello, current_time, time_plus
    
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', hello),
    url(r'^time/$', current_time),
    url(r'^time/plus/(\d{1,2})/$',time_plus),
    # Examples:
    # url(r'^$', 'dis6_10_11.views.home', name='home'),
    # url(r'^dis6_10_11/', include('dis6_10_11.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
