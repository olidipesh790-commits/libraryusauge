import requests
url = "https://httpbin.org/get"
response = requests.get(url, timeout=5)

print("Status code:", response.status_code)
print("Responce data:")
print(response.json())