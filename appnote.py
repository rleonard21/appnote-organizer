import sqlite3
import db

d = db.Database()

d.add_note("test title", "test description", "/path/to/file.pdf")
d.add_note("test title", "test description", "/path/to/file.pdf")
d.add_note("test title", "test description", "/path/to/file.pdf")
d.add_note("test title", "test description", "/path/to/file.pdf")
d.add_note("big test title", "test description", "/path/to/file.pdf")

print('--- print all: ---')
d.print_all()
print('--- output of search notes: ---')
d.search_notes('big title')
