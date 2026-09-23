import requests

TAGO_URL = "https://api.us-e1.tago.io/data"

DEVICE_TOKEN = "99757eea-0ae8-4091-995b-70b8aea94fbc"

headers = {
    "Device-Token": DEVICE_TOKEN,
    "Content-Type": "application/json"
}

data = [
    {
        "variable": "temperature",
        "value": 27.5,
        "unit": "°C"
    },
    {
        "variable": "humidity",
        "value": 65,
        "unit": "%"
    },
    {
        "variable": "ph",
        "value": 6.1,
        "unit": "pH"
    },
    {
        "variable": "ec",
        "value": 1.8,
        "unit": "mS/cm"
    },
    {
        "variable": "predicted_yield",
        "value": 2.8,
        "unit": "kg/plant"
    }
]

response = requests.post(
    TAGO_URL,
    headers=headers,
    json=data
)

print("Status:", response.status_code)
print("Response:", response.text)