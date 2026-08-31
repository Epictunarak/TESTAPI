import requests
import os

print("Start Script")

token = os.environ["ONETRUST_TOKEN"]

url = "https://app-apac.onetrust.com/api/template/v1/templates/e1fd8533-b1ef-487c-9e7a-6baf37b8e017/details"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    url,
    headers=headers
)

print("Status Code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print(response.text[:2000])
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Done")
