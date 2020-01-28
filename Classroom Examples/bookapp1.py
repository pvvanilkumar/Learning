from flask import Flask
import sqlite3
app = Flask(__name__)

@app.route("/books")
def books():
	sql="select * from books"
	mybooks = sqlite3.connect("mydb.db").cursor().execute(sql).fetchall()
	return str(mybooks)
@app.route("/books/delete/<bid>")
def delete(bid):
	return bid
@app.route("/addbookform")
def form():
	output = """
	<form method=post action="/addbooktodb">
	<input type="text" name="title"> Title<br>
	<input type="text" name="author"> Author<br>
	<input type="submit">
	</form>
	"""
	return output
@app.route("/addbooktodb")
def todb():
	return "Inserting book into db"

app.run()