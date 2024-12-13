from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _title = Column('title', String, nullable=False)
    content = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    magazine_id = Column(Integer, ForeignKey('magazines.id'), nullable=False)

    author = relationship("Author", backref="articles")
    magazine = relationship("Magazine", backref="articles")

    def __init__(self, author, magazine, title, content):
        self.author = author
        self.magazine = magazine
        self.title = title  
        self.content = content


    def __repr__(self):
        return f'<Article {self.title}>'
