
from google.appengine.ext import db
from datetime import datetime

class User(db.Model):
    firstname = db.StringProperty(required=True)
    lastname = db.StringProperty(required=True)
    nickname = db.StringProperty()
    password = db.StringProperty()
    email = db.EmailProperty()
    system_account = db.BooleanProperty(default=False)
    perms = db.ListProperty(int)
    gender = db.StringProperty(choices=['man', 'woman'])
    last_modification = db.DateTimeProperty(auto_now=True)












