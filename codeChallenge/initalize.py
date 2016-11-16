from peewee import *

db = SqliteDatabase('challenges.db')


class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)
    steps = IntegerField(default=1)

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Challenge], safe=True)
