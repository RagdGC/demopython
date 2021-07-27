from flask_restx import Namespace, Resource, fields

api = Namespace("municipios", description="Operaciones con municipios")

municipio = api.model(
    "municipio",
    {
        "estadoid": fields.Integer(),
        "id": fields.Integer(),
        "nombre": fields.String()
    }
)
municipios = [ {"estadoid":1, "id": 1, "nombre": "Alvaro Obregon"},
{"estadoid":1, "id": 2, "nombre": "Benito Juarez"}, 
{"estadoid":2, "id": 3, "nombre": "Cuautitlan"}, 
{"estadoid":2, "id": 4, "nombre": "Nezahualcoyotl"}
]

@api.route("/")
class municipioslista(Resource):
    @api.doc("get_municipioslista")
    @api.marshal_list_with(municipio)
    def get(self):
        """Lista todos los municipios"""
        resultado = municipios
        return resultado

@api.route("/<int:estadoid>")
@api.param("estadoid", "id del estado")
@api.response(404, "Estado no encontrado")
class getmunicipiosporestadoid(Resource):
    @api.doc("get_municipiosporestadoid")
    @api.marshal_list_with(municipio)
    def get(self, estadoid):
        """Recupera los municipios por el estadoid"""
        resultado = list(filter(lambda item: item['estadoid'] == estadoid, municipios))
        if resultado:
            return resultado
        api.abort(404)
