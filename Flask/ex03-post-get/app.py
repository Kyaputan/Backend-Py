from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items', methods=['POST'])
def items():
    if request.method == 'POST':
        data = request.get_json()
        return data
    else:
        return 'Invalid request'
    
@app.route('/World' , methods=['GET'])
def name():
    if request.method == 'GET':
        return 'Hello, World!'
    else:
        return 'Invalid request'

@app.route('/items', methods=['DELETE'])
def delete_items():
    if request.method == 'DELETE':
        return 'Item deleted'

if __name__ == '__main__':
    app.run(debug=True)
