
from google.appengine.ext import ndb
from datetime import datetime

class Person(ndb.Model):
    firstname = ndb.StringProperty(required=True)
    lastname = ndb.StringProperty(required=True)
    password = ndb.StringProperty()
    gender = ndb.StringProperty(choices=['man', 'woman'])
    active = ndb.BooleanProperty(required=True)
    pioneer = ndb.BooleanProperty()
    servant = ndb.BooleanProperty()
    elder = ndb.BooleanProperty()
    school_allow = ndb.BooleanProperty()
    master = ndb.BooleanProperty()
    slave = ndb.BooleanProperty()
    reader_only = ndb.BooleanProperty()
    baptism_date = ndb.DateProperty()
    age = ndb.IntegerProperty()
    last_modification = ndb.DateProperty(default=datetime.now())








