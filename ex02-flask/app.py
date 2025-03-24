from flask import Flask, render_template, request

app = Flask(__name__)

# Function to add two numbers
def add(a, b):
    return a + b

@app.route('/')
def home():
    return render_template('index.html')

# Post route to process data
@app.route('/api/data', methods=['POST'])
def post_data():
    try:
        a = int(request.form.get('a', 0))
        b = int(request.form.get('b', 0))
        result = add(a, b)
        return render_template("index.html", result=f"Number is: {result}")
    except ValueError:
        return "Invalid input! Please enter valid numbers."

# Get route to handle user input
@app.route('/api/get', methods=['GET', 'POST'])
def user_input():
    if request.method == 'POST':  # Fix: allow both GET and POST
        user_mail = request.form.get('userInput')  # Get input from the form
        return render_template("index.html", mail=f"Your mail is: {user_mail}")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
