from customer_test import info, freq
import plotly.graph_objects as go

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
        info['currencyAmount'], info['originationDateTime'])],
    marker={'size': 10},
    hovertemplate=
    '<i>Merchant</i>: %{text}'+
    '<br><i>Amount</i>: $%{customdata[0]}<br>'+
    '<i>Date</i>: %{customdata[1]}',
    ))

fig.update_layout(
    mapbox={
        'accesstoken': token,
        'style': "outdoors",
        'zoom': 13,
        'center':{'lon':-79.485304940,
                    'lat':43.6680668944}},
    showlegend=False)

fig.show()
