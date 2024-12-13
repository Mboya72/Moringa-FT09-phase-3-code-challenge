import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self._title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        """Validate title length (between 5 and 50 characters)."""
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = value

    @staticmethod
    def create(title, content, author_id, magazine_id):
        """Create and insert a new article into the database."""
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert a new article
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id) 
            VALUES (?, ?, ?, ?)
        ''', (title, content, author_id, magazine_id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        """Retrieve all articles from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()

        conn.close()

        return [Article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles]

    def __repr__(self):
        return f'<Article {self.title}>'

if __name__ == "__main__":

    articles = Article.get_all()
    for article in articles:
        print(article)
