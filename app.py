import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

# Load data
df = pd.read_csv('data/sample_data.csv')

# Create figure
fig = px.bar(df, x='category', y='value')

app.layout = html.Div(children=[
    html.H1(children='Data Visualization Dashboard'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)