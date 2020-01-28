import sqlite3
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
SQL = """
SELECT * FROM books WHERE bid=1
"""
cursor.execute(SQL)
print(cursor.fetchone())
SQL = """
SELECT * FROM books WHERE bid > 1
"""

print(cursor.execute(SQL).fetchmany(2))

SQL = """
SELECT * FROM books
"""

print(cursor.execute(SQL).fetchall())


cursor.close()

conn.close()