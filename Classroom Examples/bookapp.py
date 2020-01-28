from flask import Flask

app = Flask(__name__)

@app.route("/books")
def books():
	return "here is the book list"
@app.route("/books/delete/<bid>")
def delete(bid):
	return bid
@app.route("/addbookform")
def form():
	return "here is the book add form"
@app.route("/addbooktodb")
def todb():
	return "Inserting book into db"

app.run()