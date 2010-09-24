from django.conf.urls.defaults import *



urlpatterns = patterns('mylibrary.views',
    url("simple/$", "simple"),
    url("real/$", "real"),

)
