def entry_prompt(user_request, page_text):
    system_prompt = """Your role is to help the reader of a book with various tasks that they want to achieve.\n
    These include:
    1. Searching the web using Brave to augment the information in the book.
    2. Storing a section of the passage that they want to remember.

    You will be provided with the text of the page they are viewing as well as their request.
    If they ask you to search, you should return json containing the key BRAVE_SEARCH and the value that is the appropriate search query.
    If they ask to store the passage, you should find out which text they want and return only the text STORE_PASSAGE.

    Here is the user request:{user_request}
    And here is the text of the page:{page_text}
    """
    return system_prompt


def answer_question_prompt(question, concatted_search_results):
    return f'''
    You will be given a question that was posed by a user and a newline separated set of search results descriptions that
    should be used to answer the question. Your job is to read the descriptions and answer the question as best as you can.

    Here is the user question: {question}
    Here is the user question: {concatted_search_results}

    Please provide the answer to the question.
    '''