import requests

url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

try:
    response = requests.get(url, timeout=10)
    print("Status:", response.status_code)
    print(response.text[:300])

except Exception as e:
    print("ERROR:", e)