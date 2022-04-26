import requests

# response = requests.get("https://www.google.com")
# response

# response.headers

# response.text

url = 'https://www.google.com'
response = requests.get(url)
print(f'Request to {url}. Status code is {response.status_code}.')
