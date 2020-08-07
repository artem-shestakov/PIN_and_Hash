from flask_restful import Resource, fields, marshal_with
from .utils import hash_generator
from .parser import pin_parser

# The format of response
hash_fields = {
    "pin": fields.String(),
    "salt": fields.String(),
    "hash": fields.String()
}


# Handler for request
class HashApi(Resource):
    @marshal_with(hash_fields)
    def get(self):
        args = pin_parser.parse_args()
        pin_len = args["pin_len"]
        salt_len = args["salt_len"]
        if not salt_len:
            salt_len = 4
        resp = hash_generator(pin_len, salt_len)
        return resp
