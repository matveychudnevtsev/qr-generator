from flask import Blueprint, jsonify, request

bp = Blueprint('qr', __name__)

@bp.route('/', methods=['GET'])
def generate():
    data = request.args.get('data', '')
    # Placeholder for QR generation
    return jsonify({'qr': f'generated-from-{data}'})
