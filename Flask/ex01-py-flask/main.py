from flask import Flask, render_template, request, jsonify
import base64
import os

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    response = {"message": "Received", "data": data}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)