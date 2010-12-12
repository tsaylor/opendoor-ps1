from django.conf.urls.defaults import *
from piston.resource import Resource as PistonResource
from api.handlers import UserHandler, ResourceHandler, user_resourceHandler

user_resource = PistonResource(UserHandler)
resource_resource = PistonResource(ResourceHandler)
user_resource_resource = PistonResource(user_resourceHandler)

urlpatterns = patterns('',
   url(r'^user/$', user_resource),
   url(r'^user/(?P<uid>.*)/$', user_resource),
   url(r'^resource/$', resource_resource),
   url(r'^resource/(?P<name>.*)/$', resource_resource),
   url(r'^resourcelevel/$', user_resource_resource),
   url(r'^resourcelevel/(?P<uid>.*)/(?P<name>.*)/$', user_resource_resource),
)
