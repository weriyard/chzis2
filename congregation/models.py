from google.appengine.ext import db

from chzis.user.models import User

class CongregationMember(db.Model):
    user = db.ReferenceProperty(User, required=False)
    age = db.IntegerProperty()
    baptism_date = db.DateProperty()
    active = db.BooleanProperty(required=True)
    servant = db.BooleanProperty()
    elder = db.BooleanProperty()
    pioneer = db.BooleanProperty()
    school_allow = db.BooleanProperty()
    master = db.BooleanProperty()
    slave = db.BooleanProperty()
    reader_only = db.BooleanProperty()
    lector = db.BooleanProperty()
    sound_sysop = db.BooleanProperty()
    last_modification = db.DateTimeProperty(auto_now=True)



