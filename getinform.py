import requests

url = "https://app-apac.onetrust.com/api/template/v1/templates/e1fd8533-b1ef-487c-9e7a-6baf37b8e017/details"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)