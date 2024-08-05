import requests
url="https://www.wscubetech.com/"
response=requests.get(url)
print(response.status_code)