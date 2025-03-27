from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/items")
def items():
    # Read data from items.json
    with open('items.json') as file:
        data = json.load(file)
    items_list = data['items']
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True)
