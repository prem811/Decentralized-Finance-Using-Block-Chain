from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/payment')
def payment():
    return render_template('index.html')

@app.route('/repayment')
def repayment():
    return render_template('repay.html')

@app.route('/application')
def contact():
    return render_template('application.html')

if __name__ == "__main__":
    app.run(debug=True)
