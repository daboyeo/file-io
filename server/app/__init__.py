from flask import Flask

from server.app import extension


def register_extension(app: Flask):
    extension.cors.init_app(app)


def register_blueprint(app: Flask):
    from server.app.view import file_blueprint
    app.register_blueprint(file_blueprint)


def create_app():
    app = Flask("file-io")
    register_extension(app)
    register_blueprint(app)
    return app
