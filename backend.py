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
    values = request.form.get("resSearch")
    return "value:" + str( values )


if __name__ == "__main__":
    app.run(debug = True)
