from flask import Flask, escape, request, render_template
import sqlite3

#Name of select: restrict
#Name of input: resSearch

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/search.html')
def processSearch():
    return request.args.get("resSearch")


if __name__ == "__main__":
    app.run(debug = True)
