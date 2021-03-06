from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Model for pets"""
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    pet_name = db.Column(db.String(25),
                         nullable=False)
    species = db.Column(db.String(40),
                        nullable=False)
    photo_url = db.Column(db.Text,
                          default="",
                          nullable=False)
    age = db.Column(db.Text,
                    nullable=False)
    notes = db.Column(db.Text,
                      nullable=True)
    available = db.Column(db.Boolean,
                          default=True,
                          nullable=False)
