from google.appengine.ext import db

from chzis.user.models import User


class Congregation(db.Model):
    name = db.StringProperty(required=True)
    address = db.StringProperty()
    number = db.IntegerProperty()
    circuit = db.IntegerProperty()
    coordinator = db.ReferenceProperty(User, required=False)


class CongregationMember(db.Model):
    user = db.ReferenceProperty(User)
    congregation = db.ReferenceProperty(Congregation, required=False)
    age = db.IntegerProperty()
    baptism_date = db.DateProperty()
    active = db.BooleanProperty()
    servant = db.BooleanProperty()
    elder = db.BooleanProperty()
    coordinator = db.BooleanProperty()
    pioneer = db.BooleanProperty()
    school_allow = db.BooleanProperty()
    master = db.BooleanProperty()
    slave = db.BooleanProperty()
    reader_only = db.BooleanProperty()
    lector = db.BooleanProperty()
    sound_sysop = db.BooleanProperty()
    last_modification = db.DateTimeProperty(auto_now=True)


