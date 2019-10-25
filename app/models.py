from . import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ ='roles'
    id = db.Column(db.Integer,primary_key=True)
    role = db.Column(db.String(255))

    def __repr__(self):
        f'Role {self.role}'
