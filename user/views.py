
from chzis.req import BaseHandler
from chzis.user.models import User


class UserList(BaseHandler):
    def get(self):
        users = User.all()
        print users
        tpl_var = dict()
        tpl_var['users'] = users

        self.render_template('users.html', tpl_var)


