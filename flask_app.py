
import requests
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
API_BASE_URL = "http://localhost:5000"

@app.route("/")
def index():
    response = requests.get(f"{API_BASE_URL}/items")
    items = response.json()
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add_item():
    item_data = {
        "id": request.form["id"],
        "name": request.form["name"]
    }
    response = requests.post(f"{API_BASE_URL}/items", json=item_data)
    if response.status_code == 201:
        return redirect("/")
    return jsonify({"error": "Failed to add item"}), 400

@app.route("/delete/<string:item_id>")
def delete_item(item_id):
    response = requests.delete(f"{API_BASE_URL}/items/{item_id}")
    if response.status_code == 200:
        return redirect("/")
    return jsonify({"error": "Failed to delete item"}), 400

if __name__ == "__main__":
    app.run(debug=True)