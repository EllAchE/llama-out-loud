def entry_prompt(user_request, page_text):
    # TODO: if this doesn't work well we should first have a simple model handle the request and do one of 3 prompts based on that 
    system_prompt = f'Your role is to help the reader of a book with various tasks that they want to achieve.\n\
    These include:\
    1. Searching the web using Brave to augment the information in the book.\
    2. Storing a section of the passage that they want to remember.\
    3. Answering questions using your training data.\n\
    You will be provided with the text of the page they are viewing as well as their request.\
    If asked for something you can answer based on your training data, respond with a json containing the key TRAINING_DATA and your answer as the value.\
    If asked for recent information (or information outside your training data), you should return json containing the key BRAVE_SEARCH and an appropriate search query as the value.\
    If asked to store the passage, return json with the key "STORE_PASSAGE" then two more keys, "title" which should contain a suitable title\
    for the summary and "text" with the text they requested and "emoji" with a suitable emoji\n' + f"Whatever json you send should be wrapped in ``` to identify in. Here is the user request:{user_request}" + f"And here is the text of the page:{page_text}"
    
    return system_prompt

    # TODO: we don't have a note saving route yet... would be good to have it
    # TODO: an action taking route would be good too


def answer_question_prompt(question, concatted_search_results):
    return f'''
    You will be given a question that was posed by a user and a newline separated set of search results descriptions that
    should be used to answer the question. Your job is to read the descriptions and answer the question as best as you can.

    Here is the user question: {question}
    Here is the user question: {concatted_search_results}

    Please provide the answer to the question.
    '''

def create_page_summary(title, content, heading = "Summary"):
    return f'''
    You will be given a title and content for a page that you should create in Notion. Your job is to create a new page in the specified database with the title and content provided.

    Here is the title: {title}
    Here is the content: {content}
    '''