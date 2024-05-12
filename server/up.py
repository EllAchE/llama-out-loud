from flask import Flask, request
import os
from werkzeug.utils import secure_filename
from datetime import datetime



app = Flask(__name__)
UPLOAD_FOLDER = '/Users/mlc/Code/hackathon/tester'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
counter = 0

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'img' not in request.files:
        return "No file part", 400
    
    file = request.files['img']
    # if file.filename == '':
    #     return "No selected file", 400
    if file:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        _, file_extension = os.path.splitext(file.filename)
        filename = f"{timestamp}{file_extension}"
        # filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "File successfully uploaded", 200
        counter += 1
        # _, file_extension = os.path.splitext(file.filename)
        # # Create filename using only the counter
        # filename = secure_filename(f"{counter}{file_extension}")
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # counter += 1  # Increment the counter after saving the file
        # return "File successfully uploaded", 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
