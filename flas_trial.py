# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 16:04:38 2022

@author: jahna
"""


from flask import Flask
from flask import render_template, request


app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<a href='http://127.0.0.1:5000/quickstart'>QuickStart</a>"
@app.route("/quickstart")
def my_quickstart():
    return "<h1> This is my quick start page!</h1>"
app.run()


@app.route('/pythoncourse')
def python_course():
    print("Now accessing python course html")
    return render_template('python_course.html')
@app.route('/input',methods=['POST', 'GET'])  # There are two methods to transfer data from client browser to the web server
def test():
    if request.method == 'POST':  # if data is recieved from the form....
         ht = int(request.form['height'])
         age = int(request.form['age'])
         print(ht,age)
    return render_template('test.html')
app.run()