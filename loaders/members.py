from datetime import datetime
from google.appengine.ext import db, ndb
from google.appengine.tools import bulkloader
from google.appengine.ext.ndb import key
from chzis.congregation.models import CongregationMember


# class Lesson(db.Model):
#     pass


class CongregationMemberLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'CongregationMember',
                                   [
                                       ('number', lambda x: 10),
                                       ('name', lambda x: x.decode('utf-8')),
                                       ('reading', lambda x: bool(int(x))),
                                       ('demo',  lambda x: bool(int(x))),
                                       ('discourse',  lambda x: bool(int(x)))
                                       #                                    ('description', str),
                                       #                                    ('last_modification', lambda x : datetime.now)
                                   ])



loaders = [CongregationMemberLoader]