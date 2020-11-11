from mongoengine import Document, fields


class Applies(Document):
    name = fields.StringField(required=True, max_length=50)
    company = fields.StringField(required=True)
    email = fields.EmailField(required=True)
    telf = fields.StringField(required=False, min_length=9, max_length=9, null=True, blank=True)
    content = fields.StringField(required=False, null=True, blank=True)
