import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "This field is done"
}

# Gửi yêu cầu POST để tạo đối tượng mới
post_response = requests.post(endpoint, json=data) 

# Kiểm tra mã trạng thái và nội dung phản hồi
if post_response.status_code == 200:
    try:
        print(post_response.json())
    except requests.JSONDecodeError:
        print("Response content is not valid JSON.")
        print(post_response.text)
else:
    print(f"Error: {post_response.status_code}")
    print(post_response.text)
