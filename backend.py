from flask import Flask, escape, request, render_template
import query_builder as qb
import sqlite3
import time

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
    other_ingredients_list = [ing.strip() for ing in other_ingredients_list]
    expansion_set = qb.expand_exlusions(checked_ingredients)    
    full_list = list(expansion_set) + other_ingredients_list
    full_list = qb.remove_empty(full_list)
        
    query = qb.generate_search_query([food_item], full_list) 
    if len(full_list) == 0:
        query = qb.gen_generic_query([food_item])
    connection = sqlite3.connect("food_db.db")
    cursor = connection.cursor()
    
    rows = []
    for row in cursor.execute( query ):
        rows.append(row)
    amount = len( rows )
    return render_template("search.html", search_term = food_item, entries=rows, amount=amount)

@app.route("/upc_match.html")
def product_and_image():
    upc = request.args.get("upc")
    if upc == None:
        return "No products found with that upc"
    conn = sqlite3.connect("food_db.db")
    cursor = conn.cursor()
    entries = []
    print("Getting matching product: " + upc)
    query = "SELECT item, ingredients, gtin_upc from foods where gtin_upc = " + "'" + upc + "'"
    print("QUERY: " + query) 
    for iterator in cursor.execute(query):
        entries.append(iterator)
    # There should only be one entry
    entry = entries[0]
    return render_template("upc_match.html", entry=entry)

@app.route("/product_submission.html")
def route_product_submission():
    # Getting required fields for an entry
    upc = request.args.get("product_upc")
    name = request.args.get("product_name")
    manufacturer = request.args.get("product_manufacturer")
    ingredients = request.args.get("product_ingredients")
    default_source = "user:" + request.environ["REMOTE_ADDR"]
    
    
    date = time.strftime("%m/%d/%y %T")
    entry_tuple = (name, default_source, upc, manufacturer, date, date, ingredients)

    command = """INSERT INTO Experimental(item, data_source, gtin_upc, manufacturer, date_modified, ingredients)
                Values(?,?,?,?,?,?)"""
    
    connection = sqlite3.connect("food_db.db")
    cur = connection.cursor()
    cur.execute(command, entry_tuple)
    connection.commit()
    connection.close()
    return str(cur.lastrowid)

@app.route("/submit_product.html")
def route_product_page():
    return render_template("submit_product.html")



if __name__ == "__main__":
    app.static_folder = "static"
    app.run(debug = True)
