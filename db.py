import sqlite3


def _init_db():
    db = sqlite3.connect('appnotes.db')

    table = """ CREATE TABLE IF NOT EXISTS APPNOTES (
                                    id integer PRIMARY KEY,
                                    title text NOT NULL,
                                    description text,
                                    filepath text
                                ); """

    c = db.cursor()
    c.execute(table)

    return db


class Database:
    def __init__(self):
        self.db = _init_db()

    def add_note(self, title, desc, filepath):
        sql = "INSERT INTO APPNOTES (title,description,filepath) VALUES (?,?,?)"
        args = (title, desc, filepath)

        c = self.db.cursor()
        c.execute(sql, args)
        self.db.commit()

    def delete_note(self):
        pass

    def update_note(self):
        pass

    def search_notes(self, a):
        search = a.split(' ')
        c = self.db.cursor()
        template = "SELECT * FROM APPNOTES WHERE title LIKE ?"
        query = template
        terms = []

        for (i, term) in enumerate(search):
            terms.append("%" + term + "%")

            if i != len(search) - 1:
                query += " INTERSECT " + template

        c.execute(query, terms)
        self._print_cursor(c)

    def print_all(self):
        c = self.db.cursor()
        c.execute("SELECT * FROM APPNOTES")

        self._print_cursor(c)

    def _print_cursor(self, c):
        for row in c.fetchall():
            print(row)