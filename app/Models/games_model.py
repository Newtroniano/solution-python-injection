# models/user.py

from app import db

class Games(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    estoque = db.Column(db.Integer, unique=False, nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

