import requests
url='https://api.chucknorris.io/jokes/random'

Response=requests.get(url)

data = Response.json()

print(Response['se3']['priceSek'])
