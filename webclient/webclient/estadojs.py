from flask import Blueprint, render_template
import requests
urlapi = 'http://localhost:5001/'

bp = Blueprint("estadojs", __name__, url_prefix="/estadojs")

@bp.route('/')
def listas():
    endpoint = urlapi + "estados/"
    respuestaestados = requests.get(endpoint)
    endpoint = urlapi + "municipios/1"
    respuestamunicipios = requests.get(endpoint)
    return render_template("/estadojs/index.html", estados = respuestaestados.json(), municipios = respuestamunicipios.json())
    