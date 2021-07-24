from flask import Flask, json, render_template, request, redirect
import requests

app = Flask(__name__)

urlapi = 'http://localhost:5001/'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/empleados')
def listaempleados():
    endpoint = urlapi + "empleados/"
    respuesta = requests.get(endpoint)
    empleados =respuesta.json()
    return render_template("empleados/lista.html", empleados = empleados)

@app.route('/empleados/nuevo')
def nuevoempleado():
    empleado = {}
    return render_template("empleados/nuevo.html", empleado = empleado)

@app.route('/empleados/nuevo', methods=["POST"])
def guardarempleadonuevo():
    endpoint = urlapi + "empleados/"
    empleadonuevo = {"employee_id": request.form["employee_id"],
    "name": request.form["name"],
    "age": request.form["age"],
    "position": request.form["position"] }
    resultado = requests.post(endpoint, json = empleadonuevo )
    return redirect("/empleados")

@app.route('/empleados/<int:id>')
def consultarempleado(id):
    endpoint = urlapi + "empleados/" + str(id)
    respuesta = requests.get(endpoint)
    empleado =respuesta.json()
    return render_template("empleados/consulta.html", empleado = empleado)

@app.route('/empleados/<int:id>/editar')
def editarempleado(id):
    endpoint = urlapi + "empleados/" + str(id)
    respuesta = requests.get(endpoint)
    empleado =respuesta.json()
    return render_template("empleados/editar.html", empleado = empleado)

@app.route('/empleados/<int:id>/editar', methods=["POST"])
def guardarempleado(id):
    endpoint = urlapi + "empleados/" + str(id)
    empleadoactualizar = {"employee_id": request.form["employee_id"],
    "name": request.form["name"],
    "age": request.form["age"],
    "position": request.form["position"] }
    resultado = requests.put(endpoint, json = empleadoactualizar )
    return redirect("/empleados")

@app.route('/empleados/<int:id>/eliminar')
def eliminarempleado(id):
    endpoint = urlapi + "empleados/" + str(id)
    respuesta = requests.get(endpoint)
    empleado =respuesta.json()
    return render_template("empleados/eliminar.html", empleado = empleado)

@app.route('/empleados/<int:id>/eliminar', methods=["POST"])
def eliminarempleadoapi(id):
    endpoint = urlapi + "empleados/" + str(id)
    respuesta = requests.delete(endpoint)
    return redirect("/empleados")

@app.route('/javascript')
def listas():
    endpoint = urlapi + "estados/"
    respuestaestados = requests.get(endpoint)
    endpoint = urlapi + "municipios/1"
    respuestamunicipios = requests.get(endpoint)
    return render_template("/javascript/index.html", estados = respuestaestados.json(), municipios = respuestamunicipios.json())