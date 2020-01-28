from flask import Flask

app=Flask(__name__)
@app.route("/")
def abcd():
	return "Hello from Flask"

app.run(debug=True,port=4000)