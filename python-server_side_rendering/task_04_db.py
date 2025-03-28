import sqlite3
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to fetch products from SQLite
def fetch_products_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        return f"Database error: {str(e)}"

# Function to fetch products from a JSON file (simulated here)
def fetch_products_from_json():
    # Simulated JSON data
    products = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
        {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
    ]
    return products

# Function to fetch products from a CSV file (simulated here)
def fetch_products_from_csv():
    # Simulated CSV data
    products = []
    with open('products.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            products.append({
                "id": int(row['id']),
                "name": row['name'],
                "category": row['category'],
                "price": float(row['price'])
            })
    return products

@app.route('/')
def display_products():
    source = request.args.get('source', '').lower()

    if source == 'sql':
        # Fetch data from SQLite database
        data = fetch_products_from_sql()
        if isinstance(data, str):  # Error case (e.g., database issue)
            return render_template('product_display.html', error_message=data)
    elif source == 'json':
        # Fetch data from JSON
        data = fetch_products_from_json()
    elif source == 'csv':
        # Fetch data from CSV
        data = fetch_products_from_csv()
    else:
        return render_template('product_display.html', error_message="Wrong source")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
