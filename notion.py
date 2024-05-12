import os
from datetime import datetime
from notion_client import Client

nc = Client(auth=os.getenv("NOTION_API_KEY"))

root_page = 'af999b3e02e0402e9698ddc4bcf81729'

def create_notion_page(title, content, emoji = "📔", heading = "Summary"):
    # Create a new page in the specified database
    page_data = {
	"parent": { "page_id": root_page },
  "icon": {
  	"emoji": emoji
  },
	"properties": {
			"title": [
				{
					"text": {
						"content": title
					}
				}
			],
	},
	"children": [
		# {
		# 	"object": "block",
		# 	"type": "heading_2",
		# 	"heading_2": {
		# 		"rich_text": [{ "type": "text", "text": { "content": heading } }]
		# 	}
		# },
		{
			"object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": content,
						}
					}
				]
			}
		}
	]
}
    new_page = nc.pages.create(**page_data)

    print("New page created with ID:", new_page["id"])
