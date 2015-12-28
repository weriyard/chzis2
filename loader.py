from datetime import datetime
from google.appengine.ext import db, ndb
from google.appengine.tools import bulkloader
from google.appengine.ext.ndb import key
from chzis.school.models import Lesson


# class Lesson(db.Model):
#     pass


class LessonLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Lesson',
                                   [('number', lambda x: x.decode('utf-8')),
                                    ('name', lambda x: x.decode('utf-8')),
#                                    ('description', str),
#                                    ('last_modification', lambda x : datetime.now)
                                   ])

    # number = ndb.IntegerProperty(required=True)
    # name = ndb.StringProperty(required=True)
    # description = ndb.StringProperty()
    # last_modification = ndb.DateProperty(default=datetime.now())

loaders = [LessonLoader]