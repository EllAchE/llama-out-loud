from flask import Flask, request
import os
import sys
from werkzeug.utils import secure_filename
from datetime import datetime
import base64
from brave import brave_req, summarizer, concat_brave_search_results
from groq_completion import groq_completion
from groq_prompts import answer_question_prompt, entry_prompt

import json

sys.path.append("../")
from ocr import ocr

app = Flask(__name__)

# CHANGE THIS TO YOUR OWN DIRECTORY
# UPLOAD_FOLDER = '/Users/mlc/Code/hackathon/tester'

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# TODO: We need to have a global state & route(s) for the voice input

global_image_text = {
    "text": None # this should be overriden by the image endpoint (before the voice endpoint is called)
}

@app.route('/voice', methods=['POST'])
def handle_voice():
    data = request.get_json()
    if 'transcript' not in data:
        return "No transcript found", 400
    transcript = data['transcript']

    # we assume that the imsage has already been processed & saved to a file (or in memory)

    type, response = process_inputs(transcript, global_image_text["text"])

    # response should be sent back to vapi/voice api
    return response, 200


# route was previously /upload
@app.route('/image', methods=['POST'])
def handle_image():
    if 'img' not in request.files:
        return "No file part", 400
    file = request.files['img']
    
    if file:
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        _, file_extension = os.path.splitext(file.filename)
        filename = f"{timestamp}{file_extension}"
        file.save(filename)

        with open(filename, "rb") as file_to_encode:
            encoded_string = base64.b64encode(file_to_encode.read()).decode("utf-8")
    
        # print(encoded_string)
        text_out = ocr(encoded_string)

        global_image_text["text"] = text_out


        return "File successfully uploaded", 200
    
    return "No file uploaded", 500

def process_inputs(ocr_text, question = "what books has shel silverstein written in the past year?"): 
    init_prompt = entry_prompt(question, ocr_text)
    groq_res = groq_completion(init_prompt)

    if ("BRAVE_SEARCH" in groq_res):
        brave_res_obj = json.loads(groq_res)
        brave_query = brave_res_obj["BRAVE_SEARCH"]

        # get results from brave
        brave_response = brave_req(brave_query)
        concatted_brave = concat_brave_search_results(brave_response)

        # make the brave results useful before sending to voice endpoint
        voice_response = answer_question_prompt(question, concatted_brave)

        return "BRAVE_SEARCH", voice_response
    elif ("STORE_PASSAGE" in groq_res):
        # here we should reference the most recent text data & use notion to store it
        return "STORE_PASSAGE", "I've stored the passage in Notion!"
    elif ("TRAINING_DATA" in groq_res):
        training_data_obje = json.loads(groq_res)
        res = training_data_obje["TRAINING_DATA"]
        # here we should immediately respond to the user based on what is in the training data
        return "TRAINING_DATA", res
    else:
        raise ValueError("Invalid groq response")

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
