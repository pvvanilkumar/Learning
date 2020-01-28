from flask import Flask
import time
app = Flask(__name__)

@app.route("/hi")
def hi():
	return "hello from flask"

@app.route("/")
def hello():
	return "Welcome to flask"
@app.route("/now")
def now():
	now =  time.ctime(time.time())
	return str(now)
@app.route("/wish/<name>")
def wish(name):
	return "Good morning {}".format(name)

app.run()