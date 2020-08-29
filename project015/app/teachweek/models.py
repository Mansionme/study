from app import db

class TeachWeek(db.Model):
    __tablename__ = "teach_weeks"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    term = db.Column(db.String(30), nullable=False, unique=True)
    week_start = db.Column(db.Date, nullable=False, unique=True)
    week_end = db.Column(db.Date, nullable=False, unique=True)
    # week_end = db.Column(db.DateTime, nullable=False, default=time.strftime("%Y-%m-%d", time.localtime()))
    weekno_term = db.Column(db.String(30), nullable=False, unique=True)
    week_no = db.Column(db.Integer, nullable=False, unique=True)

    def __init__(self, term, week_start, week_end, weekno_term, week_no):
        self.term = term
        self.week_start = week_start
        self.week_end = week_end
        self.weekno_term = weekno_term
        self.week_no = week_no

    def to_json(self):
        result = {
            'id': self.id,
            'term': self.term,
            'week_start': self.week_start,
            'week_end': self.week_end,
            'weekno_term': self.weekno_term,
            'week_no': self.week_no,
        }
        return result