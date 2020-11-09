from django.db import models
from mongoengine import Document, fields


class Rooms(Document):
    name = fields.StringField(required=True, max_length=50)
    id_manager = fields.IntField(required=False)
    street = fields.StringField(required=True)
    capacity = fields.IntField(required=True)
    rows = fields.IntField(required=True)
    columns = fields.IntField(required=True)
    distance_between_seats = fields.FloatField(required=False, default=0.2)
    seats_size = fields.FloatField(required=False, default=0.7)
