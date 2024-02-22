#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class that stores amenities of each place"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize class instance"""
        super().__init__(*args, **kwargs)
