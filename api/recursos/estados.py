from flask_restx import Namespace, Resource, fields

api = Namespace("estados", description="Operaciones con estados")

estado = api.model(
    "estado",
    {
        "id": fields.Integer(),
        "nombre": fields.String()
    }
)
estados = [{"id": 1, "nombre": "CDMX"}, 
{"id": 2, "nombre": "EDOMEX"}]

@api.route("/")
class estadoslista(Resource):
    @api.doc("get_estadoslista")
    @api.marshal_list_with(estado)
    def get(self):
        """Lista todos los estado"""
        resultado = estados
        return resultado


#     @api.doc("delete_empleado")
#     @api.marshal_with(empleado)
#     def delete(self, id):
#         """Elimina un empleado por su id"""
#         empleadoeliminar = EmployeeModel.query.filter_by(employee_id=id).first()
#         if empleadoeliminar:
#             db.session.delete(empleadoeliminar)
#             db.session.commit()
#             return 201
#         api.abort(404)

#     @api.doc("put_empleado")
#     @api.expect(empleado)
#     @api.marshal_with(empleado)
#     def put(self, id):
#         """Actualiza los datos de un empleado por su id"""
#         empleadoactualizar = EmployeeModel.query.filter_by(employee_id=id).first()
#         if empleadoactualizar:
#             reg = api.payload
#             empleadoactualizar.employee_id = reg['employee_id']
#             empleadoactualizar.name = reg['name']
#             empleadoactualizar.age = reg['age']
#             empleadoactualizar.position = reg['position']
#             db.session.merge(empleadoactualizar)
#             db.session.commit()
#             return 201
#         api.abort(404)