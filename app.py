from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import dash

app = dash.Dash(__name__, )

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server


cards = html.Div(
    [
        dbc.Card(
            dbc.CardBody("This is some text within a card body"),
            style={"width": "18rem", 'height':'20.78rem'},
        ),
        dbc.Card("This is also within a body",
                 body=True, style={"width": "30rem", 'height': '3rem'}),
    ]
)



app.layout = dbc.Container(cards)

if __name__ == "__main__":
    app.run_server(debug=True)
