from django.db import models
from mongoengine import Document, fields


class Events(Document):
    _id = fields.StringField(primary_key=True, disabled=False)
    name = fields.StringField(required=True, max_length=50)
    logo = fields.URLField(required=False)
    date = fields.StringField(required=True)
    hourIni = fields.StringField(required=True)
    hourEnd = fields.StringField(required=True)
    minPrice = fields.IntField(required=True)
    maxPrice = fields.IntField(required=True)
    measures = fields.ListField(required=False)
    ratings = fields.FloatField(required=False, null=True, max_value=5, min_value=0)
    link = fields.StringField(required=False, null=True)
    seats = fields.StringField(required=False)
    id_manager = fields.IntField(required=False)
    id_room = fields.StringField(required=True)

