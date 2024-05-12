from flask import Flask, request
import requests
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
from notion import create_notion_page
from ocr import ocr

app = Flask(__name__)

# CHANGE THIS TO YOUR OWN DIRECTORY
# UPLOAD_FOLDER = '/Users/mlc/Code/hackathon/tester'

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# TODO: We need to have a global state & route(s) for the voice input

global_image_text = {
    "text": None # this should be overriden by the image endpoint (before the voice endpoint is called)
}

@app.route('/webhook', methods=['POST'])
def handle_voice():
    data = request.get_json()
    if 'transcript' not in data:
        return "No transcript found", 400
    transcript = data['key']

    # we assume that the imsage has already been processed & saved to a file (or in memory)

    type, response = process_inputs(transcript, global_image_text["text"])

    url = "http://localhost:3001/trigger"

    payload = json.dumps({
      "message": f"<SPEAK>{response}",
    })
    headers = {
      'Content-Type': 'application/json'
    }

    # hit vapi
    an_m = requests.request("POST", url, headers=headers, data=payload)

    # response should be sent back to vapi/voice api
    return an_m, 200


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
    print("received all inputs, processing...")
    init_prompt = entry_prompt(question, ocr_text)
    groq_res = groq_completion(init_prompt)
    print("groq_res", groq_res)

    groq_json = parse_json_from_groq(groq_res)

    if ("BRAVE_SEARCH" in groq_res):
        print("Groq routed to BRAVE_SEARCH")
        brave_query = groq_json["BRAVE_SEARCH"]

        # get results from brave
        brave_response = brave_req(brave_query)
        concatted_brave = concat_brave_search_results(brave_response)

        # make the brave results useful before sending to voice endpoint
        voice_response = answer_question_prompt(question, concatted_brave)

        return "BRAVE_SEARCH", voice_response
    elif ("STORE_PASSAGE" in groq_res):
        print("Groq routed to STORE_PASSAGE")
        nested = groq_json["STORE_PASSAGE"]
        title = nested["title"]
        requested_text = nested["text"]
        emoji = nested["emoji"]
        create_notion_page(title, requested_text, emoji)
        # here we should reference the most recent text data & use notion to store it
        return "STORE_PASSAGE", "I've stored the passage in Notion!"
    elif ("TRAINING_DATA" in groq_res):
        print("Groq routed to TRAINING_DATA")
        res = groq_json["TRAINING_DATA"]
        # here we should immediately respond to the user based on what is in the training data
        return "TRAINING_DATA", res
    else:
        raise ValueError("Invalid groq response")

def parse_json_from_groq(groq_res):
    # split the ```json``` from the groq response
    
    groq_res = groq_res.split("```json")[1] if "```json" in groq_res else groq_res.split("```")[1]
    groq_res = groq_res.split("```")[0]
    groq_json = json.loads(groq_res)
    return groq_json

test_input = '''
It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way—in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.

There were a king with a large jaw and a queen with a plain face, on the throne of England; there were a king with a large jaw and a queen with a fair face, on the throne of France. In both countries it was clearer than crystal to the lords of the State preserves of loaves and fishes, that things in general were settled for ever.

It was the year of Our Lord one thousand seven hundred and seventy-five. Spiritual revelations were conceded to England at that favoured period, as at this. Mrs. Southcott had recently attained her five-and-twentieth blessed birthday, of whom a prophetic private in the Life Guards had heralded the sublime appearance by announcing that arrangements were made for the swallowing up of London and Westminster. Even the Cock-lane ghost had been laid only a round dozen of years, after rapping out its messages, as the spirits of this very year last past (supernaturally deficient in originality) rapped out theirs. Mere messages in the earthly order of events had lately come to the English Crown and People, from a congress of British subjects in America: which, strange to relate, have proved more important to the human race than any communications yet received through any of the chickens of the Cock-lane brood. 
'''

process_inputs(test_input, "save from It was the best to age of foolishness")
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
