from mongoengine import fields, Document


class Ratings(Document):
    _id = fields.StringField(primary_key=True, disabled=False)
    author = fields.StringField(required=True)
    rate = fields.FloatField(required=True, max_value=5, min_value=0)
    comment = fields.StringField(required=False, null=True, blank=True, max_length=256)
    id_event = fields.StringField(required=False, null=True, blank=True, max_length=256)
