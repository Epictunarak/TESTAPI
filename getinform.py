import os
import sys
import requests

BASE_URL = "https://app-apac.onetrust.com"
TEMPLATE_ID = "e1fd8533-b1ef-487c-9e7a-6baf37b8e017"

client_id = os.environ["ONETRUST_CLIENT_ID"].strip()
client_secret = os.environ["ONETRUST_CLIENT_SECRET"].strip()

token_response = requests.post(
    f"{BASE_URL}/api/access/v1/oauth/token",
    data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    },
    headers={
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    },
    timeout=30,
)

print("Token status:", token_response.status_code)

if not token_response.ok:
    print("Token response:", token_response.text[:2000])
    sys.exit(1)

access_token = token_response.json()["access_token"]

response = requests.get(
    f"{BASE_URL}/api/template/v1/templates/{TEMPLATE_ID}/details",
    headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    },
    timeout=30,
)

print("GET status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Response:", response.text[:2000])

response.raise_for_status()
