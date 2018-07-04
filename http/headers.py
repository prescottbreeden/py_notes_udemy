import requests
from types import SimpleNamespace

url = "https://icanhazdadjoke.com"
res = requests.get(url, headers={"Accept": "application/json"})

# print(res.text)
res_data = res.json()
data = SimpleNamespace(**res_data)

print(data.joke)
