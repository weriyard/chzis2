from datetime import datetime
from google.appengine.ext import db, ndb
from google.appengine.tools import bulkloader
from google.appengine.ext.ndb import key
from chzis.congregation.models import Congregation



class CongregationLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Congregation',
                                   [
                                       ('name', lambda x: x.decode('utf-8')),
                                   ])


loaders = [CongregationLoader]