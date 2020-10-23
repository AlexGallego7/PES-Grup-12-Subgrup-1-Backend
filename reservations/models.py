from django.db import models
from mongoengine import Document, fields


class Reservations(Document):
    _id = fields.StringField(primary_key=True, disabled=False)
    user = fields.StringField(required=True)
    event = fields.StringField(required=True)
    seat_number = fields.ListField(required=True)
    transport = fields.StringField(required=True)
    hour = fields.StringField(required=True)
    id_review = fields.StringField(required=False)
    id_route = fields.StringField(required=False)