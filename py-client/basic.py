import requests

endpoint = "http://localhost:8000/api/"

get_respone = requests.post(endpoint,
params = {
    "username": "TrungTR ",
    "password": "12345678"}
) #HTTP request
# print(get_respone.headers)
# print(get_respone.text) 
# print(get_respone.status_code)
print(get_respone.json())