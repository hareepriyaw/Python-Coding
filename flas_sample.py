from flask import Flask

app=Flask(__name__)
@app.route("/")
def helloworld1():
    return "<a href='http://127.0.0.1:5000/quickstart'>QuickStart</a>"
@app.route("/quickstart")
def my_quickstart():
    return "<h1> This is my quick start page!</h1>"
app.run()

