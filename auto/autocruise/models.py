from __future__ import unicode_literals

from django.db import models
from mongoengine import *


class CruiseData(Document):
    data = StringField(required=True)
    empty = StringField(required=True,max_length=0)
    from_place = StringField(required=True,max_length=150)
    full_name = StringField(required=True,max_length=150)
    numb = StringField(required=True,max_length=150)
    tel = StringField(required=True,max_length=150)
    to_place = StringField(required=True,max_length=150)
    note = StringField(required=True,max_length=1550)
