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
    food_item = request.args.get("food_item")
    checked_ingredients = request.args.getlist("checked_ing")
    other_ingredient_text = request.args.get("other_ings")
    other_ingredients_list = other_ingredient_text.split(",")

    
    return "value:" + str( values )


if __name__ == "__main__":
    app.run(debug = True)
