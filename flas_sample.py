"""
from flask import Flask

app=Flask(__name__)
@app.route("/")
def helloworld1():
    return "<a href='http://127.0.0.1:5000/quickstart'>QuickStart</a>"
@app.route("/quickstart")
def my_quickstart():
    return "<h1> This is my quick start page!</h1>"
app.run()

"""
"""
from flask import Flask, request, escape

inst=Flask(__name__)

@inst.route('/')
def hello():
    name=request.args.get("name", "world")
    return f'Hello, {escape(name)}!'
"""
from flask import Flask

def create_firstapp():
    initial_file=flask(__name__)
    return initial_file