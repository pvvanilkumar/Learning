import sqlite3
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
SQL = """

CREATE TABLE books(
bid INTEGER AUTO INCREMENT PRIMARY KEY,
title TEXT,
author TEXT
)

"""
cursor.execute(SQL)
cursor.close()
conn.close()