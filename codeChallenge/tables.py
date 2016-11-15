from peewee import *

db = SqliteDatabase('challenges.db')


class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)

    class Meta:
        database = db
