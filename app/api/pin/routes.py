from flask_restful import Resource, fields, marshal_with
from .utils import hash_generator

hash_fields = {
    "pin": fields.Integer(),
    "salt": fields.String(),
    "hash": fields.String()
}


class HashApi(Resource):
    @marshal_with(hash_fields)
    def get(self):
        resp = hash_generator()
        return resp
