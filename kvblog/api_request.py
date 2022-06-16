import requests
import pprint

response = requests.get('http://127.0.0.1:8000/api/v0/hh_requests/', auth=('user', '21412141us'))

pprint.pprint(response.json())

# token = '15549b9bfc64dbb1008048534562d5ee4bd74dde'
# headers = {'Authorization': f'Token {token}'}
# response = requests.get('http://127.0.0.1:8000/api/v0/hh_requests/', headers=headers)
# # response = requests.get('http://127.0.0.1:8000/api/v0/hh_requests/')
# pprint.pprint(response.json())