from chzis.req import BaseHandler


class Index(BaseHandler):
    def get(self):

        self.render_template('index.html', {})

