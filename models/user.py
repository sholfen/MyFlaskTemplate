import requests
import json
import flask_login as flask_login
from flask import redirect
from functools import wraps
from controllers import login_manager
import modules.config_module as config_module


def get_user_from_session(user_id):
    user = User()
    user.id = user_id
    user.name = user_id
    return user


role_types = {0: 'normal_user', 1: 'admin', 2: 'root' }
# it's a decorator
def required_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user  = flask_login.current_user
            role_type = role_types[user.role_type]
            if user.role_type_name in roles:
                print('you have the permission')
            else:
                print('you do not have permission')
                # todo: raise error
                return redirect('/')
            return f(*args, **kwargs)
        return wrapped
    return wrapper


class User(flask_login.UserMixin):
    
    email = ''
    role_type = 0
    user_id = 0
    role_type_name = ''
    user_id = 0

    @staticmethod
    def get_user_info(user_id):
        return None

    @staticmethod
    def get(user_id):
        return get_user_from_session(user_id)
