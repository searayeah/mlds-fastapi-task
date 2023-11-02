import requests

pk = 80
url = f"http://127.0.0.1:8000/dog/{pk}"
data = {"name": "vanyavanya", "pk": pk, "kind": "bulldog"}

response = requests.patch(url, json=data)


print(response.text)
