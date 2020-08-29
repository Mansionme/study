from app import db

class TeachPlan(db.Model):
    __tablename__ = "teach_plan"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    subject = db.Column(db.String(100), nullable=False, unique=True)
    remarks = db.Column(db.String(200), default='' )
    department_id = db.Column(db.String(10), nullable=False)
    status = db.Column(db.Boolean(),nullable=False, default=False)
    # department_id = db.Column(db.DateTime, nullable=False, default=time.strftime("%Y-%m-%d", time.localtime()))
    week_no = db.Column(db.Integer, nullable=False)

    def __init__(self, subject, remarks, department_id, status, week_no):
        self.subject = subject
        self.remarks = remarks
        self.department_id = department_id
        self.status = status
        self.week_no = week_no

    def to_json(self):
        result = {
            'id': self.id,
            'subject': self.subject,
            'remarks': self.remarks,
            'department_id': self.department_id,
            'status': self.status,
            'week_no': self.week_no,
        }
        return result