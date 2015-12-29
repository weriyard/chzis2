import time

from google.appengine.ext import db, ndb
from google.appengine.tools import bulkloader
from chzis.congregation.models import CongregationMember, Congregation
from chzis.user.models import User


class CongregationMemberLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'CongregationMember',
                                   [   ('age', lambda x: int(10)),
                                       ('ent2', str),
                                       ('ent3', str)
                                   ])

    def user_get_or_create(self, firstname, lastname):
        users = User.all()
        user = users.filter('firstname', firstname, ).filter('lastname', lastname)
        if user.count() == 0:
            user = User(firstname=firstname,lastname=lastname)
            user.put()
        else:
            user = user.get()

        return user

    def congregation_get_or_create(self, congregation_name):
        congregations = Congregation.all()
        congregation = congregations.filter('name', congregation_name)
        if congregation.count() == 0:
            congregation = Congregation(name=congregation_name)
            congregation.put()
        else:
            congregation = congregation.get()

        return congregation

    def create_entity(self, values, key_name=None, parent=None):
        firstname, lastname = values[0].decode('utf-8'), values[1].decode('utf-8')
        congregation = values[2].decode('utf-8')

        user = self.user_get_or_create(firstname, lastname)
        congregation = self.congregation_get_or_create(congregation)
        congregation_member = CongregationMember()
        congregation_member.user = user
        congregation_member.congregation = congregation
        congregation_member.put()
        time.sleep(1)
        return bulkloader.Loader.create_entity(self, values, key_name=None, parent=None)

    # def handle_entity(self, entity):
    #     print dir(entity)
    #     print entity.properties
    #     return entity

loaders = [CongregationMemberLoader]
