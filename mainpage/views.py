from chzis.req import BaseHandler
from chzis.congregation.models import Congregation, CongregationMember

class Index(BaseHandler):
    def get(self):
        congregation_members = Congregation.all()
        self.render_template('index.html', {})

