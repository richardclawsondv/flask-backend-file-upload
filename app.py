import os
from flask import Flask, request, session
from werkzeug.utils import secure_filename
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('HELLO WORLD')

ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/var/www/flask-backend-file-upload/uploads'
CORS(app, expose_headers='Authorization')


@app.route('/upload', methods=['POST'])
def fileUpload():
    target = os.path.join(app.config['UPLOAD_FOLDER'], 'test')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    session['uploadFilePath'] = destination
    try:
    	response = "Success!"
    except Exception as e:
    	response = "Error occured!"
    	
    return response


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=8000)