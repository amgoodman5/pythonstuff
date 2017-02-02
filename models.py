import datetime

from peewee import *

DATABASE = SqliteDatabase('cats.sqlite')

class Cats(Model):
    name = CharField()
    color = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Cats], safe=True)
    DATABASE.close()
