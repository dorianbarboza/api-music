from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dorian:dorian12345@localhost/api_music'
db = SQLAlchemy(app)

class Usuario(db.Model):

    #__tablename__ = 'Usuario'

    ID_Usuario = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(10), unique = False)
    password = db.Column(db.String(10), unique = False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<ID_Usuario> {}'.format(self.ID_Usuario)

    def serialize(self):
        return {
            'ID_Usuario': self.ID_Usuario,
            'username': self.username,
            'password': self.password
            }

class UsuarioResource(Resource):
    def get(self):
        try:
            users = Usuario.query.all()
            return  jsonify([e.serialize() for e in users])
        except Exception as e:
            return(str(e))

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass



api.add_resource(UsuarioResource, '/appmusic/api/v1.0/usuario/get/')

if __name__ == '__main__':
    app.run(debug = True, port = 8080, host = '127.0.0.1')
    db.create_all()
