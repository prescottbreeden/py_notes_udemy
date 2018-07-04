import requests
from types import SimpleNamespace

url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
)

# print(res.text)
res_data = res.json()
data = SimpleNamespace(**res_data)

print(data.results[0]['joke'])
