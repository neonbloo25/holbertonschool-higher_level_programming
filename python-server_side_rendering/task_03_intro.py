from flask import Flask, render_template, request, jsonify
import json
import csv

app = Flask(__name__)

# Read data from the JSON file
def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)

# Read data from the CSV file
def read_csv():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])  # Ensure ID is an integer
            row['price'] = float(row['price'])  # Convert price to float
            products.append(row)
    return products

# Route for displaying products
@app.route('/products', methods=['GET'])
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    
    if product_id:
        # Filter products by id
        product = next((p for p in products if p['id'] == product_id), None)
        if not product:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=[product])
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
