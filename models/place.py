#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
from models.review import Review
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary='place_amenity',viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            '''reviews call relationship'''
            my_list = {}
            all_review = self.review
            for review in all_review:
                if self.id == review.id:
                    my_list.append(review)
            return my_list

        @property
        def amenities(self):
             """getter amenity that returns the list of Amenity"""

            myamenities = {}
            all_amenities = self.amenities
            for a in all_amenities:
                if self.id == a.id:
                    myamenities.append(a)
            return myamenities

        @amenities.setter
        def amenities(self, obj=None):
              """Setter amenities"""

            if obj.__class__name__ == 'Amenity':
                self.amenities_ids.append(obj.id)

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey
                             ('amenities.id'),
                             primary_key=True, nullable=False))