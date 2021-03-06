from django.conf.urls import patterns, url

from views import form1, form2, form3
from views import add_post
from views import generate_bookmarklet
from views import get_json
from views import signin
from views import xref_proxy

urlpatterns = patterns('',
                       # I think these 3 should be broken out to an API URL handler so we
                       # can evolve it
                       url(r'^$', get_json, name="get_json"),

                       url(r'^form/page1/(?P<user_id>.*)/$', form1, name="form1"),
                       url(r'^form/page2/$', form2, name="form2"),
                       url(r'^form/page3/$', form3, name="form3"),


                       url(r'^post/$', add_post, name="add_post"),
                       url(r'^signin/$', signin, name="signin"),
                       url(r'^bookmarklet/(?P<user_id>.*).js$',
                           generate_bookmarklet,
                           name="generate_bookmarklet"),
                       url(r'^xref_proxy/(?P<doi>.*)',
                           xref_proxy,
                           name="xref_proxy"),
                       )
