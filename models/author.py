import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name):
        """Insert a new author into the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """Retrieve all authors from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        rows = cursor.fetchall()
        conn.close()
        return [cls(row['id'], row['name']) for row in rows]

    def __repr__(self):
        return f'<Author {self.name}>'

authors = Author.get_all()
for author in authors:
    print(author)
