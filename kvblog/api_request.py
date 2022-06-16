import requests
import pprint

# response = requests.get('http://127.0.0.1:8000/api/v0/hh_requests/', auth=('user', '21412141us'))
#
# pprint.pprint(response.json())

token = '9cca971fc7b4260d6fe0e8009af26da6e53e9ccf'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/hh_requests/', headers=headers)
# response = requests.get('http://127.0.0.1:8000/api/v0/hh_requests/')
pprint.pprint(response.json())