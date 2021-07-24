from flask_restx import Api
from .empleados import api as empleado_api
from .estados import api as estado_api
from .municipios import api as municipio_api

api = Api(version='1.0', title='Demo general API',
    description='Demo general API',
)

api.add_namespace(empleado_api)
api.add_namespace(estado_api)
api.add_namespace(municipio_api)
