from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qrhandler.views.home', name='home'),
    # url(r'^qrhandler/', include('qrhandler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<qrmsg>\w+)/$', 'qrhandler.views.get_qr_code', {'qrtype': 'wide'}),
    url(r'^fit/(?P<qrmsg>\w+)/$', 'qrhandler.views.get_qr_code', {'qrtype': 'fit'}),

)
