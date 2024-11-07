from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/comeco')
def comeco():
    return render_template('comeco.html')

if __name__ == '__main__':
    app.run(debug=True)
