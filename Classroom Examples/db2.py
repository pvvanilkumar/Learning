import sqlite3
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
SQL = """
INSERT INTO books(title,author)
VALUES('Wings of Fire','Abdul Kalam')
"""
cursor.execute(SQL)
cursor.close()
conn.commit()
print("{} rows inserted".format(cursor.rowcount))
conn.close()