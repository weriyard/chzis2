from datetime import datetime

from google.appengine.ext import db
from chzis.congregation.models import CongregationMember


class Lesson(db.Model):
    number = db.IntegerProperty(required=True)
    name = db.StringProperty(required=True)
    reading = db.BooleanProperty()
    demo = db.BooleanProperty()
    discourse = db.BooleanProperty()
    description = db.StringProperty()
    last_modification = db.DateTimeProperty(auto_now=True)


class Background(db.Model):
    number = db.IntegerProperty(required=True)
    name = db.StringProperty(required=True)
    description = db.StringProperty()
    last_modification = db.DateTimeProperty(auto_now=True)

class StudentProfile(db.Model):
    person = db.ReferenceProperty(CongregationMember, required=True)
    lesson = db.ReferenceProperty(Lesson, required=True)
    lesson_passed = db.BooleanProperty()
    lesson_comments = db.StringProperty()
    background = db.ReferenceProperty(Background)
    description = db.StringProperty()
    creation_date = db.DateProperty()
    presentation_date = db.DateProperty()
    topic = db.StringProperty()
    last_modification = db.DateTimeProperty(auto_now=True)
