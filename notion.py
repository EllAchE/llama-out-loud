import os
from notion_client import Client

nc = Client(auth=os.getenv("NOTION_API_KEY"))

root_page = 'af999b3e02e0402e9698ddc4bcf81729'

def create_notion_page():
    # Create a new page in the specified database
    new_page = nc.pages.create(**{
        "parent": {"page_id": root_page},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "Your Page Title"
                        }
                    }
                ]
            },
            "Description": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Your description here"
                        }
                    }
                ]
            }
            # Add more properties here if your database has more columns
        }
    })

    print("New page created with ID:", new_page["id"])

create_notion_page()