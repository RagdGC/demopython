from flask_restx import Namespace, Resource, fields
from models import EmployeeModel, db
import datetime

api = Namespace("empleados", description="Operaciones con empleados")

empleado = api.model(
    "empleado",
    {
        "id": fields.Integer(),
        "employee_id": fields.Integer(),
        "name": fields.String(),
        "age": fields.Integer(),
        "position": fields.String(),
        "fechaingreso": fields.Date()
    }
)

@api.route("/")
class empleadoslista(Resource):
    @api.doc("get_empleadoslista")
    @api.marshal_list_with(empleado)
    def get(self):
        """Lista todos los empleados"""
        resultado = EmployeeModel.query.all()
        return resultado

    @api.doc("post_empleado")
    @api.expect(empleado)
    @api.marshal_with(empleado)
    def post(self):
        """Alta de empleado"""
        reg = api.payload
        empleadonuevo = EmployeeModel(employee_id= reg['employee_id'], 
        name= reg['name'], age=reg['age'], position=reg['position'], 
        fechaingreso= datetime.datetime.strptime(reg['fechaingreso'], '%Y-%m-%d').date())
        db.session.add(empleadonuevo)
        db.session.commit()
        return

@api.route("/<int:id>")
@api.param("id", "id del empleado")
@api.response(404, "Empleado no encontrado")
class getempleado(Resource):
    @api.doc("get_empleado")
    @api.marshal_with(empleado)
    def get(self, id):
        """Recupera un empleado por su id"""
        resultado = EmployeeModel.query.filter_by(employee_id=id).first()
        if resultado:
            return resultado
        api.abort(404)

    @api.doc("delete_empleado")
    @api.marshal_with(empleado)
    def delete(self, id):
        """Elimina un empleado por su id"""
        empleadoeliminar = EmployeeModel.query.filter_by(employee_id=id).first()
        if empleadoeliminar:
            db.session.delete(empleadoeliminar)
            db.session.commit()
            return 201
        api.abort(404)

    @api.doc("put_empleado")
    @api.expect(empleado)
    @api.marshal_with(empleado)
    def put(self, id):
        """Actualiza los datos de un empleado por su id"""
        empleadoactualizar = EmployeeModel.query.filter_by(employee_id=id).first()
        if empleadoactualizar:
            reg = api.payload
            empleadoactualizar.employee_id = reg['employee_id']
            empleadoactualizar.name = reg['name']
            empleadoactualizar.age = reg['age']
            empleadoactualizar.position = reg['position']
            empleadoactualizar.fechaingreso = reg['fechaingreso']
            db.session.merge(empleadoactualizar)
            db.session.commit()
            return 201
        api.abort(404)