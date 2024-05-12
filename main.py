import json
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

def grok_decision_tree(groq_res: str):
    if ("BRAVE_SEARCH" in groq_res):
        brave_res_obj = json.loads(groq_res)
        brave_query = brave_res_obj["BRAVE_SEARCH"]
        return "BRAVE_SEARCH", brave_query
    elif ("STORE_PASSAGE" in groq_res):
        store_passage = json.loads(groq_res)
        return "STORE_PASSAGE", None
    elif ("TRAINING_DATA" in groq_res):
        training_data_obje = json.loads(groq_res)
        res = training_data_obje["TRAINING_DATA"]
        return "TRAINING_DATA", res
    else:
        raise ValueError("Invalid groq response")
        return None

                                                         
def main():
    shel_silverstein = '''MAGIC
 Sandra's seen a leprechaun,
 Eddie touched a troll,
 Laurie danced with witches once,
 Charlie found some goblins' gold.
 Donald heard a mermaid sing,
 Susy spied an elf.
 But all the magic I have known
 I've had to make myself'''

    init_prompt = entry_prompt("what books has shel silverstein written in the past year?", shel_silverstein)
    groq_res = groq_completion(init_prompt)

    if ("BRAVE_SEARCH" in groq_res):
        brave_res_obj = json.loads(groq_res)
        brave_query = brave_res_obj["BRAVE_SEARCH"]
        return "BRAVE_SEARCH", brave_query
    elif ("STORE_PASSAGE" in groq_res):
        store_passage = json.loads(groq_res)
        return "STORE_PASSAGE", None
    elif ("TRAINING_DATA" in groq_res):
        training_data_obje = json.loads(groq_res)
        res = training_data_obje["TRAINING_DATA"]
        return "TRAINING_DATA", res
    else:
        raise ValueError("Invalid groq response")
        return None

    p = brave_req("what books has shel silverstein written in the past year?")

    ss = concat_brave_search_results(p)

    thep = answer_question_prompt(ss, "what books has shel silverstein written in the past year?")

    groq_res = groq_completion(thep)
    print(groq_res)