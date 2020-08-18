# cob: type=views mountpoint=/
from cob import route
from tasks import task_send1
from uuid import uuid4
from flask import jsonify
from cob.project import get_project

config = get_project().config

@route('/req1')
def req1():
    uid = str(uuid4())
    config['requests'][uid] = None
    task_send1.s(uid=uid).apply_async()
    return jsonify(uid)

@route('/req1/<uid>')
def req1_response(uid):
    return config['requests'][uid]
