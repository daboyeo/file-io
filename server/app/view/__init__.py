from flask import Blueprint
from flask_restful import Api

file_blueprint = Blueprint('file', __name__, url_prefix='/file')
api = Api(file_blueprint)

from .file import File
api.add_resource(File, '')
