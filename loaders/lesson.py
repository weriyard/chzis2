from datetime import datetime
from google.appengine.ext import db, ndb
from google.appengine.tools import bulkloader
from google.appengine.ext.ndb import key
from chzis.school.models import Lesson


# class Lesson(db.Model):
#     pass


class LessonLoader(bulkloader.Loader):
    def __init__(self):
        self.handle_entity()
        bulkloader.Loader.__init__(self, 'Lesson',
                                   [
                                       ('number', lambda x: 10),
                                       ('name', lambda x: x.decode('utf-8')),
                                       ('reading', lambda x: bool(int(x))),
                                       ('demo',  lambda x: bool(int(x))),
                                       ('discourse',  lambda x: bool(int(x)))
                                       #                                    ('description', str),
                                       #                                    ('last_modification', lambda x : datetime.now)
                                   ])
        self.generate_records(filename='./lekcje.csv')



loaders = [LessonLoader]