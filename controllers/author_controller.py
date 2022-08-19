from flask import Blueprint
from main import db
from models.authors import Author

authors = Blueprint('authors', __name__, url_prefix="/authors")

@authors.route("/", methods=["GET"])
def get_books():
    # get all the books from the db
    authors_list = Author.query.all()


    return "List of authors"
