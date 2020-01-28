from flask import Flask , redirect, url_for
from random import random
import time
import sys,os
from os.path import abspath
import sqlite3




app = Flask( __name__ )

@app.route("/")
def hi():
    return "Hi from flask"

@app.route("/contact")
def hello():
    return "Hi this is python"


@app.route("/weather")
def weather():
    return "Hey its sunny here"

@app.route("/mood")
def mood():
    return "Happy holidays"

@app.route("/time")
def time1():
        now = time.ctime(time.time())
        return str(now)


@app.route("/random")
def random1():
        number = random()
        return str(number)

@app.route("/platform")
def platfrom():
        return sys.platform

@app.route("/square/<number>")
def square(number):
        output = int(number) ** 2
        return str(output)


@app.route("/srch/<file>/<text1>")
def srch(file,text1):
        return str(file + text1)

# Assignments 
@app.route("/search/<filename>/<pat>")
def searchpattern(filename,pat):
    file = os.path.join(sys.path[0],filename)
    filedata = []
    f = open(file,'r')
    for line in f:
        if pat in line:
           filedata.append(line) 
    f.close()
    return str(filedata)
    
@app.route("/book/<bid>")
def bookid(bid):
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * from books where bid = ?',bid)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return str(data)

@app.route("/booklist")
def booklist():
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    cursor.execute('SELECT title from books')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return str(data)

app.run()
