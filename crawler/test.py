from urllib.request import urlopen
import requests

response = requests.get('https://www.dart.org/')
print(response.content.decode('utf-8'))
print(response.headers['Content-Type'])

