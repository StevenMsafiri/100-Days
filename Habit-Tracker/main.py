import requests
USERNAME = "iankidubo"
TOKEN = "g322yyb23yu41nik23"
pixela_endpoint = "https://pixe.la/v1/users"


pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#Creating a user account on Pixela
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id":"graph1",
    "name": "Active time of Coding",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",

}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Creating a graph
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_parameters['id']}"

pixel_data = {
    "date": "20241016",
    "quantity": "90",
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)
