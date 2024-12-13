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

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not value:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def contributors(self):
        return [article.author for article in self.articles]

    def article_titles(self):
        if not self.articles:
            return None
        return [article.title for article in self.articles]

    def contributing_authors(self):
        authors = {}
        for article in self.articles:
            author = article.author
            authors[author] = authors.get(author, 0) + 1

        return [author for author, count in authors.items() if count > 2] or None

    def __repr__(self):
        return f'<Magazine {self.name}>'
