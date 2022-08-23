import requests

r = requests.get("https://openapi.naver.com/v1/nid/me")
print(r.text)