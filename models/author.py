from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.connection import Base


class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'
