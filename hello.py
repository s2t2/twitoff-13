# hello.py

from flask import Flask

app = Flask(__name__)

# handle requests to the home page
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    x = 2 + 2
    return f"About Me {x}"
