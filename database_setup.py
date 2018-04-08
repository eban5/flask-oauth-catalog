import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        #Returns object data in JSON
        return {
            'id' : self.id,
            'name' : self.name,
        }

class Item(Base):
    __tablename__ = 'item'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        #Returns object data in JSON
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id
        }

class User(Base):
    __tablename__ = 'user'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    email = Column(String(80), nullable = False)
    picture = Column(String(500))

    @property
    def serialize(self):
        # Serializable format
        return {
            'name'   : self.name,
            'id'    : self.id,
            'email' : self.email,
            'picture' : self.picture
        }


engine = create_engine('sqlite:///categoryapp.db')
Base.metadata.create_all(engine)
