from flask import Blueprint
from main import db
from models.authors import Author
from models.books import Book
from datetime import date

db_commands = Blueprint("db", __name__)


@db_commands.cli.command('create')
def create_db():
    # Tell SQLAlchemy to create all tables for all models in the physical DB
    db.create_all()
    print('Tables created')


@db_commands.cli.command('drop')
def drop_db():
    # Tell SQLAlchemy to drop all tables
    db.drop_all()
    print('Tables dropped')


@db_commands.cli.command('seed')
def seed_db():
    author1 = Author(
        name="Haruki Murakami",
        country="Japan",
        dob=date(day=12, month=5, year=1962)
    )
    db.session.add(author1)

    book1 = Book(
        title = "1Q84",
        genre = "novel",
        year = 1995,
        length = 300
    )
    db.session.add(book1)

    db.session.commit()

    print("tables seeded successfully ")

# note: use flask db create/ flask db drop/ flask db seed in the terminal to execute these commands