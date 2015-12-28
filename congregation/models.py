from google.appengine.ext import db
from datetime import datetime

from chzis.user.models import User

class CongregationMember(db.Model):
    user = db.ReferenceProperty(User, required=False)
    active = db.BooleanProperty(required=True)
    pioneer = db.BooleanProperty()
    servant = db.BooleanProperty()
    elder = db.BooleanProperty()
    school_allow = db.BooleanProperty()
    master = db.BooleanProperty()
    slave = db.BooleanProperty()
    reader_only = db.BooleanProperty()
    baptism_date = db.DateProperty()
    age = db.IntegerProperty()
    last_modification = db.DateProperty(default=datetime.now())


