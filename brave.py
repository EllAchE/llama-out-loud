import requests
import os

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
