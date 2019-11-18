import json
from collections import namedtuple

Customer = namedtuple('Customer', ['id', 'name'])

DATA_PATH = './data/customer1.json'

with open(DATA_PATH) as f:
    data = json.load(f)['result']
    customer1 = Customer(id=data['id'], name=data['surname']);
   
   
print(f'The customer is {customer1.name}, with id {customer1.id}')
