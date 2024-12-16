
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
collection = db["my_collection"]

@app.route("/items", methods=["GET"])
def get_items():
    items = list(collection.find({}, {"_id": 0}))
    return jsonify(items)

@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Item created"}), 201

@app.route("/items/<string:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.json
    collection.update_one({"id": item_id}, {"$set": data})
    return jsonify({"message": "Item updated"})

@app.route("/items/<string:item_id>", methods=["DELETE"])
def delete_item(item_id):
    collection.delete_one({"id": item_id})
    return jsonify({"message": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)