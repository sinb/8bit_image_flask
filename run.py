import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

rootpath = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(rootpath, 'uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER