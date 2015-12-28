
from datetime import datetime
from google.appengine.ext import ndb

from chzis.person.models import Person


class Lesson(ndb.Model):
    number = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty(required=True)
    reading = ndb.BooleanProperty()
    demo = ndb.BooleanProperty()
    discourse = ndb.BooleanProperty()
    description = ndb.StringProperty()
    last_modification = ndb.DateProperty(default=datetime.now())


class Background(ndb.Model):
    number = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty()
    last_modification = ndb.DateProperty(default=datetime.now())


class PersonSchool(ndb.Model):
    person = ndb.KeyProperty(Person, required=True)
    lesson = ndb.KeyProperty(Lesson, required=True)
    lesson_passed = ndb.BooleanProperty()
    lesson_comments = ndb.StringProperty()
    background = ndb.KeyProperty(Background)
    description = ndb.StringProperty()
    creation_date = ndb.DateProperty()
    presentation_date = ndb.DateProperty()
    topic = ndb.StringProperty()
    last_modification = ndb.DateProperty(default=datetime.now())