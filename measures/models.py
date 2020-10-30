from django.db import models
from mongoengine import Document, fields


class Measures(Document):
    name = fields.StringField(required=True, max_length=30)
    indications = fields.StringField(required=True, max_length=500)
