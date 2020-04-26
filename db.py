from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    coordinate = db.Column(db.String, nullable=False)
    traffic = db.relationship(
        'Traffic', back_populates='stores')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.coordinate = kwargs.get('coordinate', '')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'coordinate': self.coordinate,
            'traffics': [t.serialize() for t in self.traffic],
        }

    def sim_serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'coordinate': self.coordinate
        }


class Traffic(db.Model):
    __tablename__ = 'traffics'
    id = db.Column(db.Integer, primary_key=True)
    storeId = db.Column(db.Integer,  db.ForeignKey('stores.id'), primary_key=False)
    store = db.Column(db.String, nullable=False)
    hour = db.Column(db.Integer, nullable=False)
    traffic = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.due_date = kwargs.get('due_date', '')

    def serialize(self):
        course_ob = Course.query.filter_by(id=course_id).first()

        return {
            'storeId': self.id,
            'store': Store.query.filter_by(id=storeId).first().name,
            'hour': self.hour,
            'c=traffic': self.traffic
        }
