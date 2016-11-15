from peewee import *

db = SqliteDatabase('students.db')


class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db


students = [{
    'username': 'kennethlove',
    'points': 4888
}, {
    'username': 'chalkers',
    'points': 11912
}, {
    'username': 'joykesten2',
    'points': 7363
}, {
    'username': 'craigdennis',
    'points': 4079
}, {
    'username': 'davemcfarland',
    'points': 14717
}, {
    'username': 'dylancascio',
    'points': 1975
}]


def add_students():
    for student in students:
        Student.create(username=student['username'], points=student['points'])


if __name__ == "__main__":
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
