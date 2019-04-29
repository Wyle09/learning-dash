import dash
import dash_core_components as dcc
import dash_html_components as html
from iexfinance.stocks import get_historical_data
import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go


app = dash.Dash()

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()


def graph():
    input_stock = "VZ"
    df = get_historical_data(input_stock, start=start, end=end,
                             output_format="pandas")

    trace_close = go.Scatter(x=list(df.index),
                             y=list(df.close),
                             name="Close",
                             line=dict(color="#d6022c"))
    data = [trace_close]
    layout = dict(title=input_stock,
                  showlegend=False)
    fig = dict(data=data, layout=layout)
    app.layout = html.Div([
        html.Div(html.H1(children="Hello World")),
        html.Label("DASH GRAPH"),

        html.Div(
            dcc.Input(
                id="stock-input",
                placeholder="Enter a stock to be charted",
                type="text",
                value=''
            )
        ),

        html.Div(
            dcc.Dropdown(
                options=[
                    {'label': 'Candlestick', 'value': 'Candlestick'},
                    {'label': 'Line', 'value': 'Line'}
                ]
            )
        ),

        html.Div(
            dcc.Graph(id="Stock Chart",
                      figure=fig)
        )
    ])


def main():
    graph()

    if __name__ == "__main__":
        app.run_server(debug=True)


main()
