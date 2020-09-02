#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String
from models.city import City
from sqlalchemy.orm import relationship, backref
from os import environ


if "HBNB_TYPE_STORAGE" in environ.keys(
) and environ["HBNB_TYPE_STORAGE"] == "db":
    class State(BaseModel, Base):
        """
        This is the state class
        """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for k, v in kwargs.items():
                setattr(self, k, v)
else:
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade='all, delete')

        @property
        def cities(self):
            """cities class"""
            my_list = {}
            all_cities = self.cities
            for city in all_cities:
                if State.id == city.state_id:
                    list_cities.append(city)
            return list_cities
