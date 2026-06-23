import sqlite3

class NotesManager:
    def __init__(self, db_path="notes.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT, content TEXT, category TEXT)")
        self.conn.commit()

    def add_note(self, title, content, category="General"):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        self.cursor.execute("INSERT INTO notes (title, content, category) VALUES (?, ?, ?)", (title, content, category))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_all(self):
        self.cursor.execute("SELECT * FROM notes")
        return self.cursor.fetchall()

    def update_note(self, note_id, title, content, category):
        self.cursor.execute("UPDATE notes SET title=?, content=?, category=? WHERE id=?", (title, content, category, note_id))
        self.conn.commit()
        return self.cursor.rowcount

    def delete_note(self, note_id):
        self.cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def search(self, keyword):
        search_term = f"%{keyword.lower()}%"
        self.cursor.execute("SELECT * FROM notes WHERE LOWER(title) LIKE ? OR LOWER(content) LIKE ?", (search_term, search_term))
        return self.cursor.fetchall()

    def get_by_category(self, category):
        self.cursor.execute("SELECT * FROM notes WHERE LOWER(category)=?", (category.lower(),))
        return self.cursor.fetchall()

    def get_categories(self):
        self.cursor.execute("SELECT DISTINCT category FROM notes")
        return [row[0] for row in self.cursor.fetchall()]
