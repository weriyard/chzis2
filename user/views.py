import webapp2

from chzis import TPL
from user.person import Person


class PersonList(webapp2.RequestHandler):
    def get(self):
        p = Person()
        tpl = TPL.get_template('personas.html')
        self.response.write(tpl.render())
