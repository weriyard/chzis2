import webapp2

from chzis.settings import TPL


class BaseHandler(webapp2.RequestHandler):

    def render_template(self, filename, template_args):
        tpl = TPL.get_template(filename)
        self.response.write(tpl.render(template_args))

