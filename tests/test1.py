import requests

pk = 80
url = f"http://127.0.0.1:8000/dog"
data = {"name": "vanya", "pk": pk, "kind": "bulldog"}

response = requests.post(url, json=data)


print(response.text)
