from flask import Flask
import flask_login


app = Flask(__name__, template_folder='../templates', static_folder = '../resources')
app.secret_key = 'your_key'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

import user_management_controller
import home_controller
