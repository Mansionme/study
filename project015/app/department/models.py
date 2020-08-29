from app import db

class Department(db.Model):
    __tablename__ = "department"
    __table_args__ = (db.UniqueConstraint('department_name'), )
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    department_name = db.Column(db.String(100), nullable=False)

    def __init__(self, department_name):
        self.department_name = department_name  
        
    def to_json(self):
        result = {
            'id': self.id,
            'department_name': self.department_name
        }
        return result
    