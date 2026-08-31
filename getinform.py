import requests
import os

TOKEN = os.environ["ONETRUST_TOKEN"]

url = "https://app-apac.onetrust.com/api/template/v1/templates/e1fd8533-b1ef-487c-9e7a-6baf37b8e017/details"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(
    url,
    headers=headers
)

print("Status:", response.status_code)
print(response.text)
