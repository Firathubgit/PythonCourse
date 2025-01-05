import requests

url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'

response = requests.get(url)
data = response.json()
print(data['insult'])

url2 = "https://www.purgomalum.com/service/json?text={0}".format(data['insult'])
response2 = requests.get(url2, data['insult'])
data2 = response2.json()
print(data2['result'])
