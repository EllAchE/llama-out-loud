import requests
import os

'''
Things to ask about
- how big is this now
'''

def brave_req(query: str):
    url = f"https://api.search.brave.com/res/v1/web/search?q={query.replace(' ', '+')}"

    payload = {}
    headers = {
      'Accept': 'application/json',
      'Accept-Encoding': 'gzip',
      'X-Subscription-Token': os.getenv("BRAVE_API_KEY")
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

# take the brave response and concat all of the descriptiosn in the web results
def groq_response_concat():
    pass

# hits the summarizer endpoint of the brave api
def summarizer(query: str):
    url = f"https://api.search.brave.com/res/v1/web/search?q={query.replace(' ', '+')}&summary=1"

    payload = {}
    headers = {
      'Accept': 'application/json',
      'Accept-Encoding': 'gzip',
      'X-Subscription-Token': os.getenv("BRAVE_API_KEY")
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
