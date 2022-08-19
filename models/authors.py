
from main import db

class Author(db.Model):
    # define table name in db
    __tablename__ = 'authors'

    # setting the columns

    author_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    country = db.Column(db.String())
    dob = db.Column(db.Date())


