from django.db import models
from mongoengine import Document, fields


class Reservations(Document):
    _id = fields.StringField(primary_key=True, disabled=False)
    id_user = fields.IntField(required=True)
    id_event = fields.StringField(required=True)
    seat_number = fields.ListField(required=False, null=True, blank=True)
    transport = fields.StringField(required=False, null=True, blank=True)
    hour = fields.StringField(required=False, null=True, blank=True)
    id_review = fields.StringField(required=False, null=True, blank=True)
    id_route = fields.StringField(required=False, null=True, blank=True)
