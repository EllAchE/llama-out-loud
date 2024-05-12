from flask import Flask, request
import os
import sys
from werkzeug.utils import secure_filename
from datetime import datetime

sys.path.append("../")
from ocr import ocr

app = Flask(__name__)
UPLOAD_FOLDER = '/Users/mlc/Code/hackathon/tester'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
counter = 0

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'img' not in request.files:
        return "No file part", 400
    
    file = request.files['img']
    
    if file:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        _, file_extension = os.path.splitext(file.filename)
        filename = f"{timestamp}{file_extension}"
        # filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        ocr(url = "https://github.com/EllAchE/llama-out-loud/blob/ocr/image/zoom_book.png?raw=true")

        return "File successfully uploaded", 200
        
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
