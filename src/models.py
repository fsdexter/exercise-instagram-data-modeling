import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user' 
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250),nullable=False)
    mobile_number = Column(Integer, nullable=False)
    date_of_birth = Column(Integer, nullable=False)
    address = Column(String(250))
    followers = Column(Integer)
    followed = Column(Integer)
    publications = Column(Integer)
    likes = Column(Integer)
    dislikes = Column(Integer)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

    midia_scr = Column(String(250))

class Comente(Base):
    __tablename__ = 'comente'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

    text = Column(String(250))
    date = Column(Integer)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

    media_id = Column(Integer, ForeignKey('media.id'), nullable=False)
    media = relationship(Media)

    comente_id = Column(Integer, ForeignKey('comente.id'), nullable=False)
    comente = relationship(Comente)

    title = Column(String(250))
    post_text = Column(String(250))
    date = Column(Integer)
    likes = Column(Integer)
    dislikes = Column(Integer)

class Flower(Base):
    __tablename__ = 'flower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e