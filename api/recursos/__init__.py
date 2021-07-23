from flask_restx import Api
from .empleados import api as empleado_api

api = Api(version='1.0', title='Empleados API',
    description='Ejemplo Empleados API',
)

api.add_namespace(empleado_api)
