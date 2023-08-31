from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    birthday = db.Column(db.Date)
    animals = db.relationship('Animal', backref='zookeeper', lazy=True)

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)  # Consider using choices for 'grass', 'sand', 'water'
    open_to_visitors = db.Column(db.Boolean)
    animals = db.relationship('Animal', backref='enclosure', lazy=True)

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), nullable=False) 
       
