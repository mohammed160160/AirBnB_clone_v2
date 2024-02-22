#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize class instance"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
    else:
        @property
        def reviews(self):
            """Review setter"""
            from models import storage
            review_obj = storage.all('Review')
            ret = []
            for key, value in review_obj.items():
                if self.id == value.place_id:
                    ret.append(value)
            return ret
