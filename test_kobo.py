import requests

TOKEN = "8755ced3ad45faee894f6c33aac23152f97e2510"

url = "https://kf.kobotoolbox.org/api/v2/assets/axSKNztHbLySLt3jmCeFPq/data/?format=json"

headers = {
    "Authorization": f"Token {TOKEN}"
}

response = requests.get(url, headers=headers)

print("STATUS:", response.status_code)

data = response.json()

print(type(data))
print(data)
