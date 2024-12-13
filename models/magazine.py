from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base


class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'
