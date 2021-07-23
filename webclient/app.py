from flask import Flask, render_template
import requests

app = Flask(__name__)

urlapi = 'http://localhost:5001/'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/empleados')
def listaempleados():
    endpoint = urlapi + "empleados"
    respuesta = requests.get(endpoint)
    empleados =respuesta.json()
    return render_template("empleados/lista.html", empleados = empleados)

@app.route('/empleados/nuevo')
def nuevoempleado():
    return render_template("empleados/nuevo.html")

@app.route('/empleados/nuevo', methods=["POST"])
def guardarempleadonuevo():
    return render_template("empleados/nuevo.html")

@app.route('/empleados/<int:id>')
def consultarempleado(id):
    endpoint = urlapi + "empleados/" + str(id)
    respuesta = requests.get(endpoint)
    empleado =respuesta.json()
    return render_template("empleados/consulta.html", empleado = empleado)

@app.route('/empleados/<int:id>/editar')
def editarempleado(id):
    return render_template("empleados/editar.html")

@app.route('/empleados/<int:id>/eliminar')
def eliminarempleado(id):
    return render_template("empleados/eliminar.html")