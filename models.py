from peewee import *

db = PostgresqlDatabase(
    'evil',
    user='myuser',
    password='mypass',
    host='localhost'
)

class Evil(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField(null=True)

    class Meta:
        database = db
        db_table = 'evil_tb'
        order_by = ('id',)

