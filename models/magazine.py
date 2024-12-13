from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base


class Magazine(Base):
    __tablename__ = 'magazines'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column('name', String, nullable=False)
    _category = Column('category', String, nullable=False)

    articles = relationship('Article', backref='magazine', lazy=True)

    def __init__(self, name, category):
        self._name = name
        self._category = category
        
    @property
    def id(self):
        return self.id    

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f'<Magazine {self.name}>'
