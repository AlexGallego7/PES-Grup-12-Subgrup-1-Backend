from django.db import models
from mongoengine import Document, fields


class Tutorial(Document):
    title = fields.StringField(max_length=70, blank=False, default='')
    description = fields.StringField(max_length=200, blank=False, default='')
    published = fields.BooleanField(default=False)

