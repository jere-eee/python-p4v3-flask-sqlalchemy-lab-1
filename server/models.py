from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, Integer, MetaData, String
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(SerializerMixin, db.Model):
    __tablename__ = "earthquakes"
    
    id = Column(Integer, primary_key=True)
    magnitude = Column(Float)
    location = Column(String)
    year = Column(Integer)
    
    def __repr__(self):
        return f'Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}'