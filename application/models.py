from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    
    
    def __init__(self, notes):
        self.notes = notes

    def __repr__(self):
        return '<Data %r>' % self.notes

class Loaners(db.Model):
    id_loaner_name = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=False)
    surname = db.Column(db.String(128), index=True, unique=False)
    
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Data %r>' % self.name


        
