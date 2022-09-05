from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Employee(db.Model):
    table_name = "Employee"

    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # ☛ Req -2 : Create db object from SQLAlchemy class
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # id = db.Column(db.Integer)
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # ☛ Req -3 : Define column employee_id with unique key constraint, this should be of type integer
    # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String())

    def init(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position

    def repr(self):
        return f"{self.name}:{self.employee_id}"