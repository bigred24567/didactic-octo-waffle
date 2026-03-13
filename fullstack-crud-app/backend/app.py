from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message":"Welcome to my Python full stack app!"})

@app.route('/api/data')
def get_data():
    data = {"key": "value"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
