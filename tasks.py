# cob: type=tasks
from cob import task
from models import Req

@task()
def task_send1(uid):
    Req(uid).send1()
