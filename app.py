from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/kid')
def kid():
    return render_template('kid.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/menloungewear')
def menloungewear():
    return render_template('menloungewear.html')

@app.route('/menshirts')
def menshirts():
    return render_template('menshirts.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/womendresses')
def womendresses():
    return render_template('womendresses.html')

@app.route('/womenkurtas')
def womenkurtas():
    return render_template('womenkurtas.html')

@app.route('/womenloungewear')
def womenloungewear():
    return render_template('womenloungewear.html')

@app.route('/menhoodies')
def menhoodies():
    return render_template('menhoodies.html')

if __name__ == '__main__':
    app.run(debug=True)
