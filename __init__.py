from flask import Flask

from .backend.config import DefaultConfig   # Konfigurasi
from .backend.extensions import *           # Ekstensi, misalnya SQLAlchemy()
from .backend.models import Pengguna        # Model

def create_app(conf=DefaultConfig):
    app = Flask(__name__)
    app.config.from_object(conf)

    db.init_app(app)
    migrate.init_app(app, db)
    loginm.init_app(app)

    @loginm.user_loader
    def muatkan_pengguna(id):
        return Pengguna.query.get(int(id))

    # Dimana semua Blueprint didaftarkan
    with app.app_context():
        from . import login, dasbor
        app.register_blueprint(login.bp)
        app.register_blueprint(dasbor.bp)

    return app
