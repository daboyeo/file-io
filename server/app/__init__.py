from flask import Flask


def register_blueprint(app: Flask):
    from server.app.view import file_blueprint
    app.register_blueprint(file_blueprint)


def create_app():
    app = Flask("file-io")
    register_blueprint(app)
    return app
