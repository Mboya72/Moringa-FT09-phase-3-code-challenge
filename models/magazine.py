import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def create(cls, name, category):
        """Insert a new magazine into the database."""
        conn = get_db_connection()  
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """Retrieve all magazines from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines')
        rows = cursor.fetchall()
        conn.close()
        return [cls(row['id'], row['name'], row['category']) for row in rows]  

    def __repr__(self):
        return f"<Magazine {self.name} ({self.category})>"

Magazine.create('Tech Weekly', 'Technology')

magazines = Magazine.get_all()
for magazine in magazines:
    print(magazine)
