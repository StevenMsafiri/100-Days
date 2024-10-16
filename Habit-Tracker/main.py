import requests
from datetime import datetime

from dateutil.utils import today

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

this_day = datetime.today()
leo = this_day.strftime("%Y%m%d")

pixel_endpoint = f"{graph_endpoint}/{graph_parameters['id']}"

pixel_data = {
    "date": leo,
    "quantity": input("How many minutes today? "),
}


response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

# update_endpoint = f"{pixel_endpoint}/{leo}"
#
# update_data = {
#     "quantity": "55",
# }
#
# updated_response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(updated_response.text)

