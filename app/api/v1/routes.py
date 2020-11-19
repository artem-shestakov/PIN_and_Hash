from flask import Blueprint, request, current_app
from .utils import hash_generator

api_v1_bp = Blueprint(
    'api_v1',
    __name__,
    url_prefix='/api/v1'
)


@api_v1_bp.route('/pin')
def get_pin():
    pin_len = request.args.get('pin_len')
    salt_len = request.args.get('salt_len')
    if not salt_len:
        salt_len = current_app.config['SALT_LEN']
    if not pin_len:
        pin_len = current_app.config['PIN_LEN']
    resp = hash_generator(int(pin_len), int(salt_len))
    current_app.logger.info(f"{request.method} {request.base_url} Request PIN and Hash from {request.remote_addr}")
    return resp
