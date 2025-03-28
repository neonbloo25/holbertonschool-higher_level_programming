#!/usr/bin/env python3
from flask import Flask, render_template, request
import json, csv, sqlite3

app = Flask(__name__)

def read_json():
    try:
        with open("products.json") as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    products = []
    try:
        with open("products.csv", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        return []
    return products

def read_sql():
    products = []
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except Exception:
        return []
    return products

@app.route("/products")
def display_products():
    source = request.args.get("source")
    id_param = request.args.get("id")

    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    elif source == "sql":
        products = read_sql()
    else:
        return render_template("product_display.html", error="Wrong source")

    if id_param:
        try:
            id_num = int(id_param)
            products = [p for p in products if p["id"] == id_num]
            if not products:
                return render_template("product_display.html", error="Product not found")
        except ValueError:
            return render_template("product_display.html", error="Invalid ID format")

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    
    app.run(debug=True, port=5000)
