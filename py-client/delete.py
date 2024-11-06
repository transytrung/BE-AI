import requests

product_id = input("what is the product id you want to use?\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')
    
if product_id:
    endpoint = "http://localhost:8000/api/products/1/"
    get_respone = requests.get(endpoint) 
    print(get_respone.json())