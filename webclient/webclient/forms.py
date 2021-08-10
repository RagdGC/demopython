import datetime
from flask import Blueprint, render_template, json, redirect
import requests
from flask.helpers import url_for
from werkzeug import datastructures
from wtforms import validators
from wtforms.fields.core import DateField
import datetime

urlapi = 'http://localhost:5001/'

bp = Blueprint("forms", __name__, url_prefix="/forms")

@bp.route('/')
def index():
    return render_template("/forms/index.html")

@bp.route('/<int:id>/editar')
def editarempleado(id):
    endpoint = urlapi + "empleados/" + str(id)
    respuesta = requests.get(endpoint)
    datos = respuesta.json()
    empleado = {
        'employee_id': datos['employee_id'],
        'name': datos['name'],
        'age': datos['age'],
        'position':  datos['position'],
        'fechaingreso':  datetime.date.fromisoformat(datos['fechaingreso'])
    }
    form = EmpleadoForm(data=empleado)
    return render_template("forms/editar.html", form = form)

@bp.route('/<int:id>/editar', methods=["POST"])
def guardarempleado(id):
    form = EmpleadoForm()
    if form.validate():
        endpoint = urlapi + "empleados/" + str(id)
        empleadoactualizar = {"employee_id": form.employee_id.data,
        "name": form.name.data,
        "age": form.age.data,
        "position": form.position.data,
        "fechaingreso": form.fechaingreso.data.isoformat() }
        resultado = requests.put(endpoint, json = empleadoactualizar)
        return redirect(url_for("empleados.listaempleados"))
    return render_template("forms/editar.html", form = form)

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class EmpleadoForm(FlaskForm):
    employee_id = IntegerField('Id Empleado', validators=[DataRequired()])
    name = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")])
    age = IntegerField('Edad', validators=[DataRequired(), NumberRange(min=13, max=90, message="La edad debe estar entre 13 y 90")])
    position = StringField('Puesto', validators=[DataRequired()])
    fechaingreso = DateField('Fecha Ingreso', format= '%Y-%m-%d')
