from chzis.req import BaseHandler


class CongregationMembers(BaseHandler):
    def get(self):
        self.render_template('congregationMembers.html', {})

