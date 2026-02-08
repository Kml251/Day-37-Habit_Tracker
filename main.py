import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# 1. Load the variables from the .env file
load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Create an account on the Pixela
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# Create a graph for your own project
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Studying Python",
    "unit": "Hour",
    "type": "float",
    "color": "ajisai",
}
# Keep secret your token using headers key
headers = {
    "X-USER-TOKEN": TOKEN,
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

today = datetime(year=2026, month=2, day=4) # This is for changing time to post a value different time
#today = datetime.now()

# Post value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"), # strftime is a function that replace the formatted yyyymmdd
    "quantity": "2.75"
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
# Update the data
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "10.50",
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# Delete the data
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)