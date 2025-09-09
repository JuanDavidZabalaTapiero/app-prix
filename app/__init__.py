from flask import Flask

from .blueprints import register_blueprints
from .config import Config
from .extensions import db, migrate


def create_app(config_class=Config):
    """
    Application factory function.

    Creates and configures the Flask application instance.

    Returns:
        Flask: A Flask application instance.
    """

    app = Flask(__name__)

    # == CONFIGURACIÓN ==
    app.config.from_object(config_class)

    # == INICIALIZAR EXTENSIONES ==
    db.init_app(app)
    migrate.init_app(app, db)

    # == IMPORTAR MODELOS ==
    from . import models  # noqa: F401

    # == REGISTRAR BLUEPRINTS ==
    register_blueprints(app)

    return app
