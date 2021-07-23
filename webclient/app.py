from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/empleados')
def listaempleados():
    return render_template("empleados/lista.html")

@app.route('/empleados/nuevo')
def nuevoempleado():
    return render_template("empleados/nuevo.html")