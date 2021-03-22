from server.app import create_app
from server.const import RUN_SETTINGS

if __name__ == '__main__':
    app = create_app()
    app.run(**RUN_SETTINGS)
