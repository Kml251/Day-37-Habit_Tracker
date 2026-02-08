import requests

USERNAME = "ky251"
TOKEN = "fknsdknkfdnkaalmd"

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

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Studying Python",
    "unit": "Hour",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# Create a graph for your own project
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
