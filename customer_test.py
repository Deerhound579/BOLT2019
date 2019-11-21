import json
import re
from datetime import datetime as dt
from collections import namedtuple, Counter

Customer = namedtuple('Customer', ['id', 'name'])
Transaction = namedtuple('Transaction', ['lon',
                                         'lat',
                                         'storeName',
                                         'amount',
                                         'date', # a datetime object, allow easy access of month, day
                                         'tags'
                                        ])
reg = re.compile('\d{4}-\d{2}-\d{2}')


CUSTOMER = './data/rich_girl.json'
TRANS = './data/rich_girl.json'

# with open(DATA_PATH) as f:
#     data = json.load(f)['result']
#     customer1 = Customer(id=data['id'], name=data['surname'])

# infomation for plots
info = {'locationLongitude':[],
        'locationLatitude':[],
        'merchantName':[],
        'currencyAmount':[],
        'originationDateTime':[],
        'categoryTags':[]}

data_with_geo, tags = {}, set()
transacs = [] # Store information for each transaction as a Transaction object
   
with open(TRANS) as f:
    result = json.load(f)['result']


# Filter out transactions without geo info
data_with_geo = [ data for data in result if 'locationLongitude' in data]


def createDate(input: str):
    m = reg.match(input).group(0)
    return dt.strptime(m, '%Y-%m-%d')

reg = re.compile('\d{4}-\d{2}-\d{2}')
for data in data_with_geo:
    transacs.append(
        Transaction(*[createDate(data[k]) if k == 'originationDateTime' else data[k] for k in info.keys()])
    )


for k in info.keys():
    info[k] = [ data[k] for data in data_with_geo]

# Count frequencies for merchants
freq = Counter()
for m in info['merchantName']:
    freq[m] += 1


