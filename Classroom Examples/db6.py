import sqlite3
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
SQL = """
INSERT INTO books(title,author)
VALUES('Wings of Fire','Abdul Kalam')
"""
try:
	cursor.execute(SQL)
except Exception as err:
	print(type(err))
	print(err)
	print("Exception occured. Rolling back")
	conn.rollback()
else:
	cursor.close()
	print("All is well. Committing")
	conn.commit()
	print("{} rows inserted".format(cursor.rowcount))
finally:
	conn.close()