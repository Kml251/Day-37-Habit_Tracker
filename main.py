import requests

USERNAME = "ky251"
TOKEN = "fknsdknkfdnkaalmd"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Create an account on the Pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
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
# Create a graph for your own project
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# Post value to the graph
pixel_data = {
    "date": "20260208",
    "quantity": "2.30"
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

