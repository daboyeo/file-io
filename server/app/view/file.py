import os
from uuid import uuid4
from flask import request, send_from_directory
from flask_restful import Resource
from werkzeug.utils import secure_filename


class File(Resource):
    image_path = "./"
    extensions = {"png", "jpg"}

    def get(self):
        uuid = request.args.get("uuid")
        print(uuid)
        return send_from_directory(directory=File.image_path, filename=uuid)

    def post(self):
        uuid = str(uuid4())
        file = request.files['file']

        file_name = secure_filename(file.filename)
        extension = file.filename.split(".")[-1].lower()

        if extension not in File.extensions:
            return {'message': 'unsupported extension name'}, 400

        file.save(os.path.join(File.image_path, uuid+file_name))
        return {'file_uuid': uuid}, 201
