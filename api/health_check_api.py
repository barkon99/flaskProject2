from flask import Blueprint, jsonify

health_check_blueprint = Blueprint('health_check_blueprint', __name__)


@health_check_blueprint.route('/api/health', methods=['GET'])
def health_check():
    return jsonify(status='OK')
