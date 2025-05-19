from flask import Blueprint, jsonify

bp = Blueprint('files', __name__)

@bp.route('/', methods=['GET'])
def list_files():
    return jsonify([])
