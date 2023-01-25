from flask import Flask

import settings
from api.aggregates_api import aggregates_blueprint
from api.health_check_api import health_check_blueprint

app = Flask(__name__)
app.register_blueprint(health_check_blueprint)
app.register_blueprint(aggregates_blueprint)


def configure_app(flask_app):
    flask_app.config['LOGIN'] = settings.LOGIN
    flask_app.config['PASSWORD'] = settings.PASSWORD


def initialize_app(flask_app):
    configure_app(flask_app)


if __name__ == '__main__':
    initialize_app(app)
    app.run()
