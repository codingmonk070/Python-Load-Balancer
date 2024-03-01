from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is server 1!"

@app.route('/other')
def other():
    return "This is server 1 handling another route!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
