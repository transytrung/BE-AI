import requests

endpoint = "http://localhost:8000/api/update-programs/"

response = requests.post(endpoint)

if response.status_code == 200:
    print("Dữ liệu đã được cập nhật.")
else:
    print(f"Error: {response.status_code}")
