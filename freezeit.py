from app import app
from flask_frozen import Freezer

freezer = Freezer(app)


@freezer.register_generator
def page():
    pages = ["index", "about", "contact"]
    for p in pages:
        yield {'page': p}

if __name__ == '__main__':
    freezer.freeze()
