import os
import jinja2

APP_PATH = os.path.join(os.path.dirname(__file__))

APPS = ['congregation',
        'school',
        'user',
        'mainpage']

LAYOUT_DIR = 'layout'


def get_templates_path():
    templates_paths = []
    for app in APPS:
        tpl_path = os.path.join(APP_PATH, app, 'templates')
        templates_paths.append(tpl_path)
    return templates_paths

templates = get_templates_path()
templates.append(os.path.join(APP_PATH, LAYOUT_DIR))

TPL = jinja2.Environment(
    loader=jinja2.FileSystemLoader(templates),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
