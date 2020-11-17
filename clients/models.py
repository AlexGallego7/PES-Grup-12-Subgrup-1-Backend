from mongoengine import Document, fields


class Clients(Document):
    _id = fields.IntField(primary_key=True, disabled=False)
    username = fields.StringField(required=True)
    age = fields.IntField(required=False, min_value=14)
    country = fields.StringField(required=False, null=True, blank=True)
