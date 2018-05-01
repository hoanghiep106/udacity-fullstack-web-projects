import os
from jinja import jinja_env


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)
