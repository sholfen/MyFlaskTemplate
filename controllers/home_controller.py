from flask import render_template
import flask
import flask_login
from flask_login import login_required
from controllers import app
import models.user as user
from models.demoDb.demo_db_model import DemoDBModel
controller_name = 'Home'


@app.route("/")
@login_required
def index_method():
    return render_template('./home/Index.pyhtml',
            logout_template='./partial_templates/partial_logout_template.pyhtml')


@app.route("/{0}/list_all_employee".format(controller_name))
def list_all_employee_api():
    model = DemoDBModel()
    db_result = model.list_all_employee()
    json_result = {
            'status': True,
            'data': []
    }
    for item in db_result:
        json_result['data'].append({
                'first_name': item['FirstName'],
                'last_name': item['LastName'],
                'city': item['City']
        })
    return flask.jsonify(json_result)


@app.route("/{0}/test_demo_db3".format(controller_name))
@app.route("/{0}/test_demo_db".format(controller_name))
def test_demo_db():
    model = DemoDBModel()
    db_result = model.list_album_title()
    for item in db_result:
        print(item['Title'])
    return 'test'

"""
@app.after_request
def add_custom_header(response):
    # response.headers["X-Frame-Options"] = "SAMEORIGIN"
    # response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers.add('test-a', 'testtest')
    return response
"""
