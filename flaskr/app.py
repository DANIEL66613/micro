import sys
if not sys.getdefaultencoding().lower() == 'utf-8':
    sys.setdefaultencoding('utf-8')

from flask import Flask
from .config import db, DevelopmentConfig
from .controllers import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    register_blueprints(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
