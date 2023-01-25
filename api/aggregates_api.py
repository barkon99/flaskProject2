import logging.config
import os

from flask_httpauth import HTTPBasicAuth
from flask import request, Blueprint
import settings

auth = HTTPBasicAuth()
aggregates_blueprint = Blueprint('aggregates_blueprint', __name__)

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


@aggregates_blueprint.route('/aggregates', methods=['POST'])
@auth.login_required
def get_aggregates():
    if settings.LOG_RESPONSE:
        log.info('Response body: %s', request.get_json())
    return request.get_json()


@auth.verify_password
def authenticate(username, password):
    if username and password:
        if username == settings.LOGIN and password == settings.PASSWORD:
            return True
        else:
            return False
    return False


@aggregates_blueprint.before_request
def log_request_info():
    if settings.LOG_REQUEST:
        log.info('Request body: %s', request.get_json())

