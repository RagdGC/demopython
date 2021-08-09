from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class EmployeeModel(db.Model):
    __tablename__ = "empleado"
 
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))
 
    def __init__(self, employee_id,name,age,position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position
 
    def __repr__(self):
        return f"{self.name}:{self.employee_id}"

class EstadoModel(db.Model):
    __tablename__ = "estado"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))

    def __init__(self) -> None:
        super().__init__()

    def __init__(self, id, nombre ):
        self.id = id
        self.nombre = nombre

    def __repr__(self):
        return f"{self.id} {self.nombre}" 

class MunicipioModel(db.Model):
    __tablename__ = "municipio"

    id = db.Column(db.Integer, primary_key=True)
    estado_id = db.Column(db.Integer)
    nombre = db.Column(db.String(100))

    def __init__(self) -> None:
        super().__init__()

    def __init__(self, id, estado_id, nombre ):
        self.id = id
        self.estado_id = estado_id
        self.nombre = nombre

    def __repr__(self):
        return f"{self.estado_id}-{self.id} {self.nombre}" 