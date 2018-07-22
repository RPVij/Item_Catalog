# Importing all required files:
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Creating a variable base
Base = declarative_base()


# making CLASS for User(Base)
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# making class for Sports(Base)
class Sports(Base):
    __tablename__ = 'sports'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    sports_player = relationship('SportsPlayer', cascade='all, delete-orphan')

    # Properties of Sports(Base) class
    @property
    def serialize(self):
        # Returning object data in easily serializeable format
        return {
            'name': self.name,
            'id': self.id,
        }


# making class for SportsPlayer(Base)
class SportsPlayer(Base):
    __tablename__ = 'sports_player'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    country = Column(String(200))
    rank = Column(String(8))
    sports_id = Column(Integer, ForeignKey('sports.id'))
    sports = relationship(Sports)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # Properties of SportsPlayer(Base) class
    @property
    def serialize(self):
        # Returning object data in easily serializeable format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'country': self.country,
            'rank': self.rank,
        }

# Creating a variable engine
engine = create_engine('sqlite:///sports.db')


Base.metadata.create_all(engine)
