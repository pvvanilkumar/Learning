from flask import Flask, request, redirect, url_for, render_template
import sqlite3
app = Flask(__name__)

@app.route("/books")
def books():
	sql="select * from books"
	mybooks = sqlite3.connect("mydb.db").cursor().execute(sql).fetchall()
	return render_template("books.html",books=mybooks)
@app.route("/books/delete/<bid>")
def delete(bid):
	sql="delete from books where bid = {}".format(bid)
	conn = sqlite3.connect("mydb.db")
	conn.cursor().execute(sql)
	conn.commit()
	return redirect(url_for('books'))
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
@app.route("/addbooktodb",methods=["POST"])
def todb():
	author = request.form.get('author')
	title = request.form.get('title')
	sql="insert into books(title,author) values('{}','{}')".format(title,author)
	conn = sqlite3.connect("mydb.db")
	conn.cursor().execute(sql)
	conn.commit()
	return redirect(url_for('books'))

app.run()