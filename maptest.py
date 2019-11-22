import plotly.graph_objects as go
from colorfunctions import tagToColor, create_hue, create_lumin, create_color
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

colors = create_color(create_hue(tagToColor(info['categoryTags'])), create_lumin(info['frequency']))
sizes = create_size(info['currencyAmount'])
# you need your own token
token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w'

DATA = 'data/transactions_of_customer1.json'

fig = go.Figure()

fig.add_trace(
    go.Scattermapbox(
    name='',
    mode='markers',
    lat=info['locationLatitude'],
    lon=info['locationLongitude'],
    text=info['merchantName'],
    customdata=[(t1, t2, t3) for t1, t2, t3 in zip(
        info['currencyAmount'], info['frequency'], info['categoryTags'])],
    marker={'color':colors,
            'size': sizes},

    hovertemplate=
    '%{text} <i>(%{customdata[2]}</i>)'+
    '<br><i>You spent</i> $%{customdata[0]:.2f}<br>' +
    '<i>You went here</i> %{customdata[1]} times',
))


fig.update_layout(
    mapbox={
        'accesstoken': token,
        'style': "light",
        'zoom': 13,
        'center': {'lon': -79.485304940,
                   'lat': 43.6680668944}},
    showlegend=False)

fig.show()
