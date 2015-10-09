# -*- coding: utf-8 -*-
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
from flask import send_from_directory    
from werkzeug import SharedDataMiddleware
from to8bit import *
from palette import *

rootpath = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(rootpath, 'uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

preset = Palette()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    # return render_template('base.html')                                            
    return '''
    <!doctype html>
    <title>8bit 图片转换</title>
    <h1>上传文件</h1>
    <h2>转换时间大约20-40秒</h2>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
      选择块: <input type="text" name="fname" />
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    pic = to8bit()
    pic.loadImg(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    palette = preset('NES')
    img = pic.pixelize(palette, 8)
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], '8bit', '8bit_'+filename))    
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], '8bit'), '8bit_'+filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)                               