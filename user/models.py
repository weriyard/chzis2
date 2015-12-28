
from google.appengine.ext import db
from datetime import datetime

class User(db.Model):
    firstname = db.StringProperty(required=True)
    lastname = db.StringProperty(required=True)
    nickname = db.StringProperty()
    password = db.StringProperty()
    email = db.EmailProperty()
    gender = db.StringProperty(choices=['man', 'woman'])
    last_modification = db.DateProperty(default=datetime.now())












