from flask import Blueprint, render_template, request, redirect
from flask.helpers import url_for
import requests
urlapi = 'http://localhost:5001/'

bp = Blueprint("empleados", __name__, url_prefix="/empleados")

@bp.route('/')
def listaempleados():
    endpoint = urlapi + "empleados/"
    respuesta = requests.get(endpoint)
    empleados =respuesta.json()
    return render_template("empleados/lista.html", empleados = empleados)

@bp.route('/nuevo')
def nuevoempleado():
    empleado = {}
    return render_template("empleados/nuevo.html", empleado = empleado)

@bp.route('/nuevo', methods=["POST"])
def guardarempleadonuevo():
    endpoint = urlapi + "empleados/"
    empleadonuevo = {"employee_id": request.form["employee_id"],
    "name": request.form["name"],
    "age": request.form["age"],
    "position": request.form["position"],
    "fechaingreso": request.form["fechaingreso"]
     }
    resultado = requests.post(endpoint, json = empleadonuevo )
    return redirect(url_for("empleados.listaempleados"))

@bp.route('/<int:id>')
def consultarempleado(id):
    endpoint = urlapi + "empleados/" + str(id)
    respuesta = requests.get(endpoint)
    empleado =respuesta.json()
    return render_template("empleados/consulta.html", empleado = empleado)

@bp.route('/<int:id>/editar')
def editarempleado(id):
    endpoint = urlapi + "empleados/" + str(id)
    respuesta = requests.get(endpoint)
    empleado =respuesta.json()
    return render_template("empleados/editar.html", empleado = empleado)

@bp.route('/<int:id>/editar', methods=["POST"])
def guardarempleado(id):
    endpoint = urlapi + "empleados/" + str(id)
    empleadoactualizar = {"employee_id": request.form["employee_id"],
    "name": request.form["name"],
    "age": request.form["age"],
    "position": request.form["position"] }
    resultado = requests.put(endpoint, json = empleadoactualizar )
    return redirect(url_for("empleados.listaempleados"))

@bp.route('/<int:id>/eliminar')
def eliminarempleado(id):
    endpoint = urlapi + "empleados/" + str(id)
    respuesta = requests.get(endpoint)
    empleado =respuesta.json()
    return render_template("empleados/eliminar.html", empleado = empleado)

@bp.route('/<int:id>/eliminar', methods=["POST"])
def eliminarempleadoapi(id):
    endpoint = urlapi + "empleados/" + str(id)
    respuesta = requests.delete(endpoint)
    return redirect(url_for("empleados.listaempleados"))