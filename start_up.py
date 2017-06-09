from flask import url_for
import logging
import logging.config
import yaml
import flask_login

def get_logger(logger_name):
    with open('config/logger.config') as f:
        D = yaml.load(f)
    D['handlers']['file']['filename'] = 'log/default.log'
    logging.config.dictConfig(D)
    logger = logging.getLogger(logger_name)
    return logger

def add_functions_to_jinja(app):
    user = flask_login.current_user
    app.jinja_env.globals.update(login_user=user)

def start_up(app):
    logger = get_logger('dashboard_logger')
    app.logger.addHandler(logger)
    add_functions_to_jinja(app)
    print('start_up')
