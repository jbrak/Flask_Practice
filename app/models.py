from app import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, index = True, unique = True)
    temp = db.Column(db.Float, index = True)


    def __repr__(self):
        return '<Data {}>'.format(self.date)
