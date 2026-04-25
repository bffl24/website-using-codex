from pathlib import Path

from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    from expense_tracker.routes import main_bp

    app.register_blueprint(main_bp)

    return app
