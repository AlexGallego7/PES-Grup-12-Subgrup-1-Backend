from mongoengine import fields, Document


class Managers(Document):
    _id = fields.IntField(primary_key=True, disabled=False)
    username = fields.StringField(required=True)
    nif = fields.StringField(required=False, null=True, blank=True, min_length=9, max_length=9)
    telf = fields.StringField(required=False, null=True, blank=True, min_length=9, max_length=9)
