from urllib import response
import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2019-01-01&endtime=2021-01-02&latitude=51.51&longitude=-0.12&maxradiuskm=2000'
response = requests.get(url, headers={'Accept':'application/json'})

# print(response.text)
# print(type(response.json()))

data = response.json()
print(data['features'][1]['properties']['place'])