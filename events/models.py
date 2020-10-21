from django.db import models
from mongoengine import Document, fields


class Events(Document):
    _id = fields.StringField(primary_key=True, disabled=False)
    name = fields.StringField(required=True)
    street = fields.StringField(required=True)
    date = fields.StringField(required=True)
    hourIni = fields.StringField(required=True)
    hourEnd = fields.StringField(required=True)
    prize = fields.FloatField(required=True)
    measures = fields.StringField(required=False, null=True)
    ratings = fields.IntField(required=False, null=True, max_value=5, min_value=0)
    link = fields.StringField(required=False, null=True)

