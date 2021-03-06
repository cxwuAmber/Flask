
from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nickname = db.Column(db.String(20),index = True,unique=True)
    email = db.Column(db.String(120),index = True,unique = True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)