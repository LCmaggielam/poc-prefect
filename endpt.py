import requests

host = "https://adb-2661458153180226.6.azuredatabricks.net"  # Replace with your instance
token = "dapi4d5c313e496ebec70d0f77afc2474391-2"  # Replace with your access token

url = f"{host}/api/2.0/jobs/list"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())