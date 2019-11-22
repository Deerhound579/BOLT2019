import plotly.graph_objects as go
from colorfunctions import create_hue, create_lumin, create_color
from customer_test import merchants
from sizefunction import create_size

info = {'categoryTags': [],
        'locationLongitude': [],
        'locationLatitude': [],
        'merchantName': [],
        'merchantId': [],
        'currencyAmount': [],
        'originationDateTime': [],
        'frequency': []
        }

for m in merchants.keys():
    info['categoryTags'].append(merchants[m].tags[0])
    info['locationLongitude'].append(merchants[m].lon)
    info['locationLatitude'].append(merchants[m].lat)
    info['merchantName'].append(merchants[m].name)
    info['merchantId'].append(merchants[m].store_id)
    info['currencyAmount'].append(merchants[m].amount)
    info['frequency'].append(merchants[m].frequency)

hue = create_hue(info['categoryTags'])
lumin = create_lumin(info['frequency'])

# you need your own token
token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w'

DATA = 'data/transactions_of_customer1.json'

fig = go.Figure(go.Scattermapbox(
    name='',
    mode='markers',
    lat=info['locationLatitude'],
    lon=info['locationLongitude'],
    text=info['merchantName'],
    customdata=[(t1, t2) for t1, t2 in zip(
        info['currencyAmount'], info['frequency'])],
    marker={'color': create_color(hue, lumin),
            'size': create_size(info['currencyAmount'])},

    hovertemplate=
    '<i>Merchant</i>: %{text}' +
    '<br><i>Amount</i>: $%{customdata[0]}<br>' +
    '<i>Frequency</i>: %{customdata[1]} time(s)',
))

fig.update_layout(
    mapbox={
        'accesstoken': token,
        'style': "outdoors",
        'zoom': 13,
        'center': {'lon': -79.485304940,
                   'lat': 43.6680668944}},
    showlegend=False)

fig.show()
