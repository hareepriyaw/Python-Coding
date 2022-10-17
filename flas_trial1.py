
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'

@app.route('/lowcaloriefoods')
def listing_LCF():
    return render_template('lowcaloriefoods.html')
app.run()


