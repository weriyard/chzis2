from datetime import datetime
from google.appengine.ext import db, ndb
from google.appengine.tools import bulkloader
from google.appengine.ext.ndb import key
from chzis.user.models import User



class UserLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'User',
                                   [
                                       ('firstname', lambda x: x.decode('utf-8')),
                                       ('lastname', lambda x: x.decode('utf-8')),
                                   ])


loaders = [UserLoader]