from flask import Flask, jsonify, request

app = Flask(__name__)


# GET /store
@app.route('/')
def home():
    return jsonify({'message': 'hello docker'})


app.run(host='0.0.0.0', port=5000, debug=True)