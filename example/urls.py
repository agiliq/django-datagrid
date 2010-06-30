from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('blogango.urls')),
)

urlpatterns += patterns('blog_grids.views',
    url(r'^$', 'blog_grid', name='blog_grids_blog_grid'),
)

urlpatterns += patterns('django.views.static',
    (r'^site_media/(?P<path>.*)$', 'serve', { 'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
)

