import requests
from datetime import datetime
import os

username = "jianxunbak"
graphID = "graph1"
token = os.environ.get("token")
today = datetime.now().strftime("%Y%m%d")

# ---- POST REQUEST: CREATE USER ACCOUNT ---- #
# pixela_end_point = "https://pixe.la/v1/users"
# user_parameters = {
#     "token": token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_end_point, json=user_parameters)
# print(response.status_code)
# print(response.text)

# ---- POST REQUEST: CREATE A GRAPH ---- #
# pixela_graph_end_point = f"https://pixe.la//v1/users/{username}/graphs"
#
# graph_parameters = {
#     "id": graphID,
#     "name": "My Coding Graph",
#     "unit": "hours",
#     "type": "float",
#     "color": "sora"
# }
#
# headers = {
#     "X-USER-TOKEN": token
# }
# response = requests.post(url=pixela_graph_end_point, json=graph_parameters, headers=headers)
#
# print(response.status_code)
# print(response.text)

# ---- POST REQUEST: ADDING PIXELS ---- #
# add_pixel_end_point = f"https://pixe.la/v1/users/{username}/graphs/{graphID}"
#
# add_pixel_parameter = {
#     "date": today,
#     "quantity": input("how many hours did I study today?: ")
# }
#
# headers = {
#     "X-USER-TOKEN": token
# }
#
# response = requests.post(url=add_pixel_end_point, json=add_pixel_parameter, headers=headers)
# print(response.status_code)
# print(response.text)

# ---- PUT REQUEST: EDITING PIXELS ---- #
day_to_update = input("Please provide date in YYYYMMDD format of day to edit: ")

edit_pixel_end_point = f"https://pixe.la/v1/users/{username}/graphs/{graphID}/{day_to_update}"

edit_pixel_parameter = {
    "quantity": input("how many hours did I study: ")
}

headers = {
    "X-USER-TOKEN": token
}

response = requests.put(url=edit_pixel_end_point, json=edit_pixel_parameter, headers=headers)
print(response.status_code)
print(response.text)

# ---- DELETE REQUEST: EDITING PIXELS ---- #
# day = "29"
# month = "04"
# year = "2024"
#
# day_to_delete = year+month+day
# delete_pixel_end_point = f"https://pixe.la/v1/users/{username}/graphs/{graphID}/{day_to_delete}"
#
# headers = {
#     "X-USER-TOKEN": token
# }
#
# response = requests.delete(url=delete_pixel_end_point, headers=headers)
# print(response.status_code)
# print(response.text)