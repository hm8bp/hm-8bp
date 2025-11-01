from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/testimoni')
def testimoni():
    return render_template('testimoni.html')

@app.route('/stok')
def stok():
    return render_template('stok.html')

@app.route('/stok_kembar')
def stok_kembar():
    return render_template('stok_kembar.html')

@app.route('/operasional')
def operasional():
    return render_template('operasional.html')

@app.route('/panduan')
def panduan():
    return render_template('panduan.html')

@app.route('/order')
def order():
    return render_template('order.html')