from flask import Flask, request
import os
import sys
from werkzeug.utils import secure_filename
from datetime import datetime
import base64
import logging
import weave

# logging.basicConfig(level=logging.DEBUG)

sys.path.append("../")
from ocr import ocr

app = Flask(__name__)
# weave.init('llama-out-loud1')

# CHANGE THIS TO YOUR OWN DIRECTORY
UPLOAD_FOLDER = '/Users/mlc/Code/hackathon/tester'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'img' not in request.files:
        return "No file part", 400
    file = request.files['img']

    if file:
        # save the file
        print('Book detected')
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        _, file_extension = os.path.splitext(file.filename)
        filename = f"{timestamp}{file_extension}"
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)

        # read the file and encode it
        with open(save_path, "rb") as file_to_encode:
            encoded_string = base64.b64encode(file_to_encode.read()).decode("utf-8")

        # process the image OCR 
        try:
            text_out = ocr(encoded_string)
            logging.info(f"OCR output: {text_out}")
            print(text_out)
        except Exception as e:
            logging.error(f"OCR processing failed: {e}")
            return str(e), 500

        return "File successfully uploaded", 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
