# Copyright 2020 University of New South Wales, University of Sydney, Ingham Institute

# Licensed under the MIT Licence;
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

hnscc_csv = "data/hnscc.csv"

df = pd.read_csv(hnscc_csv)

fig = px.histogram(df, x="Site", color="Stage")

app.layout = html.Div(children=[
    html.H1(children='Ingham Medical Physics Coding Challenge Dashboard'),

    html.Div(children='''
        HNSCC Dataset: Histogram of patients by Site and Stage
    '''),

    dcc.Graph(
        id='stage-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
