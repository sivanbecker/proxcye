# cob: type=models
from cob import db
from urlobject import URLObject
import requests
from cob.project import get_project

config = get_project().config

class Req(db.Model):

    _EP1 = 'https://restcountries-v1.p.rapidapi.com/all'
    # _HD1 = {
    #     'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    #     'x-rapidapi-key': "<apiKey>"
    # }
    _DOGS_API = 'https://dog.ceo/api/breeds/image/random'

    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, uid):
        self.uid = uid

    def send1(self):

        res = requests.get(self._DOGS_API)
        print(res)
        res.raise_for_status()
        config['requests'][self.uid] = res.json()
