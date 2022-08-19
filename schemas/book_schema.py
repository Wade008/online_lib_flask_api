from main import ma

class BookSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["book_id", "title", "genre", "length", "year"]

# single schema
book_schema = BookSchema()
# multiple schemas
books_schema = BookSchema(many=True)

