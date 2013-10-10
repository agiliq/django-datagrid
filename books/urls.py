from django.conf.urls import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    (r'^books/', include('mylibrary.urls')),

    (r'^admin/', include(admin.site.urls)),
)
