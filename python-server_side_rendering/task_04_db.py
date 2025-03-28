import sqlite3
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to fetch products from SQLite with improved connection handling
def fetch_products_from_sql():
    try:
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            return rows
    except sqlite3.Error as e:
        return f"Database error: {str(e)}"

# Function to fetch products from a JSON file with error handling
def fetch_products_from_json():
    try:
        # Simulated JSON data
        with open('products.json', 'r') as file:
            products = json.load(file)
        return products
    except FileNotFoundError:
        return "JSON file not found."
    except json.JSONDecodeError:
        return "Error decoding JSON file."

# Function to fetch products from a CSV file with error handling
def fetch_products_from_csv():
    products = []
    try:
        with open('products.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                products.append({
                    "id": int(row['id']),
                    "name": row['name'],
                    "category": row['category'],
                    "price": float(row['price'])
                })
    except FileNotFoundError:
        return "CSV file not found."
    except csv.Error:
        return "Error reading CSV file."
    return products

@app.route('/')
def display_products():
    # Get the data source from query parameter 'source'
    source = request.args.get('source', '').lower()

    if source == 'sql':
        # Fetch data from SQLite database
        data = fetch_products_from_sql()
        if isinstance(data, str):  # Error case (e.g., database issue)
            return render_template('product_display.html', error_message=data)
    elif source == 'json':
        # Fetch data from JSON
        data = fetch_products_from_json()
        if isinstance(data, str):  # Error case (e.g., file not found or invalid JSON)
            return render_template('product_display.html', error_message=data)
    elif source == 'csv':
        # Fetch data from CSV
        data = fetch_products_from_csv()
        if isinstance(data, str):  # Error case (e.g., file not found or CSV error)
            return render_template('product_display.html', error_message=data)
    else:
        # If the source is invalid, show an error
        return render_template('product_display.html', error_message="Invalid source specified. Please choose 'sql', 'json', or 'csv'.")

    # Render the template with the fetched data
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
