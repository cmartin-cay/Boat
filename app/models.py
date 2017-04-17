from app import db

class Cunt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    votes = db.Column(db.Integer)
    reason_id = db.Column(db.Integer, db.ForeignKey('reason.id'))


class Reason(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(128), index=True)
    cunts = db.relationship('Cunt', backref='dickhead', lazy='dynamic')
