import flask
from flask import render_template
from flask import request
import flask_login
from flask_login import current_user
from controllers import app
from controllers import login_manager
import models.user
from models.user import User
import modules.config_module as config_module


controller_name = 'User'
template_path = './user_management/{0}'

def validate_user(username, password):
    if username == 'admin' and password == '1234':
        return True
    
    return False

@app.route("/{0}/Login".format(controller_name), methods=['GET', 'POST'])
def login_method():
    if request.method == 'GET':
        return render_template(
                './user_management/Login.pyhtml',
                message='')

    # get parameter from request
    username = request.form['username']
    password = request.form['password']

    # validate account and password
    if not validate_user(username, password):
        return render_template(
                './user_management/Login.pyhtml',
                message='login failed')

    # get and store user in session
    user = User()
    user.id = username
    flask_login.login_user(user)

    # validate variable next
    next_url = request.args.get('next')

    # redirect example, the value
    return flask.redirect(next_url or flask.url_for('index_method'))

@app.route("/{0}/Logout".format(controller_name))
def logout_method():
    flask_login.logout_user()
    return 'already logout'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
    return flask.redirect("/{0}/Login?next={1}".format(controller_name, request.path))
