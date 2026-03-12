from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
items = []

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    items.append(data)
    return jsonify({"message": "Item created"}), 201

if __name__ == "__main__":
    app.run(debug=True)
