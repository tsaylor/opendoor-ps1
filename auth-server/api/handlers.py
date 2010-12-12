from piston.handler import BaseHandler
from opendoor_resources.models import User, Resource, user_resource

class UserHandler(BaseHandler):
    model = User

    #def get(self, request, uid):
    #    return User.objects.get(uid=uid)

    def create(self, request):
        u = User(uid=request.POST.get('uid'), public_key=request.POST.get('public_key'))
        u.save()
        return u

class ResourceHandler(BaseHandler):
    model = Resource

class user_resourceHandler(BaseHandler):
    model = user_resource

    def read(self, request, uid, name=None):
        ret = user_resource.objects.all()
        if uid != '0':
            ret = ret.filter(user__uid = uid)
        if name:
            ret = ret.filter(resource__name = name)
        return ret

    def create(self, request, uid, name):
        u = user_resource(user = User.objects.get(uid=uid),
                          resource = Resource.objects.get(name=name),
                          level = request.POST.get('level'))
        u.save()
        return u
