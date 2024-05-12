import json

from brave import brave_req, summarizer, concat_brave_search_results
from groq_completion import groq_completion
from groq_prompts import answer_question_prompt, entry_prompt

'''
- take image
- convert image to text
- get user input (hand or no hand)
- send to groq, choose next step
a. query brave for live data
b. store passage
c. store & share
- respond to user with text confirmation of the action
'''

def main(): 
    question = "what books has shel silverstein written in the past year?"

    shel_silverstein = '''MAGIC
 Sandra's seen a leprechaun,
 Eddie touched a troll,
 Laurie danced with witches once,
 Charlie found some goblins' gold.
 Donald heard a mermaid sing,
 Susy spied an elf.
 But all the magic I have known
 I've had to make myself'''

    init_prompt = entry_prompt(question, shel_silverstein)
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
        return "STORE_PASSAGE", None
    elif ("TRAINING_DATA" in groq_res):
        training_data_obje = json.loads(groq_res)
        res = training_data_obje["TRAINING_DATA"]
        # here we should immediately respond to the user based on what is in the training data
        return "TRAINING_DATA", res
    else:
        raise ValueError("Invalid groq response")
