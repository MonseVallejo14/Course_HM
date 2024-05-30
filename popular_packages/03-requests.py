# "https://api.holamundo.io/users/"  The url is the ndpoint

# GET: To enter the URL and list
# POST: To create a user
# PUT/PATCH: To actualize
# DELETE . To delete

# API ReST:
# API: Aplication Programing Interface
# ReST: Representational State Transfer

import requests

# url = "https://jsonplaceholder.typicode.com/users"
# r = requests.get(url, timeout=10)
# # print(
# #     r.status_code,
# #     r.text,
# # )

# r = r.json()

# # for user in r:
# #     print(user["name"])

# url = "https://jsonplaceholder.typicode.com/users/1"
# r = requests.get(url, timeout=10)
# # print(r.json())

# url = "https://jsonplaceholder.typicode.com/users/"
# user = {
#     "name": "Chanchito"
# }
# r = requests.post(url, timeout=10, data=user)
# print(r.status_code)

# To enter to a protected apikey
url = "https://jsonplaceholder.typicode.com/users/2"
headers = {
    "Authorization": f"Bearer {apikey}"
}
r = requests.delete(url, timeout=10, headers=headers)
print(r.status_code)
