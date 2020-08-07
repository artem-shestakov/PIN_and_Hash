from flask_restful import reqparse
from flask import url_for

# Parser object
pin_parser = reqparse.RequestParser()
# Arguments for parsing from request
pin_parser.add_argument("pin_len", type=int, required=True, location="args",
                        help="The length of PIN code (type: int) {error_msg}")
pin_parser.add_argument("salt_len", type=int, required=False, location="args",
                        help="The length of salt code (type: int) {error_msg}")
