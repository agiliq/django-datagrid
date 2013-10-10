from django.conf.urls import *



urlpatterns = patterns('mylibrary.views',
    url("simple/$", "simple"),
    url("real/$", "real"),
    url("sortable/$", "sortable"),

)
