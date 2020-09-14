from flask import Flask
from flask import render_template, request, jsonify
import plotly
from flask import Markup
import plotly.express as px
from parser import Parser
from urllib.request import urlopen
import json
import pandas as pd

app = Flask(__name__)

parser = Parser()



@app.route('/')
def index():
    return render_template('index.html', savedData = '')




@app.route('/plot', methods = ['POST'])
def plot():
    
    savedData = {
        'fields' : parser.headers()
    }
    if (parser.timeSeries()):
        df = parser.getData()
        fig = getattr(px, request.form['type'])(df, x ='fecha', y = df.columns)
        p = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
        return render_template('index.html', plot_div = Markup(p), timeSeries = True, savedData = savedData)
    else:
        df = parser.getData()
        fig = getattr(px, request.form['type'])(df, x = request.form['x'], y = request.form['y'])
        p = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
        return render_template('index.html', plot_div = Markup(p), timeSeries = False, savedData = savedData)


@app.route('/distribution', methods = ['POST'])
def distribution():
    df = parser.getData()
    fig = getattr(px, request.form['type'])(df, x ='fecha', y = df.columns)
    p = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    return render_template('index.html', plot_div = Markup(p))


@app.route('/map', methods = ['post'])
def map():
    with urlopen('https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json') as response:
        counties = json.load(response)
    df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv",
                   dtype={'fips': str})
    fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='cases',
                            color_continuous_scale="Viridis",
                            range_color=(0, 20000),
                            mapbox_style="carto-positron",
                            zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                            opacity=0.5,
                            labels={'unemp':'unemployment rate'}
                            )
    
    p = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    return render_template('index.html', plot_div = Markup(p))
    


@app.route('/data', methods = ['POST'])
def data():
    r = request.get_json()
    parser.loadData(r['url'])
    print(parser.headers())
    return jsonify({'headers': parser.headers(), 'timeSeries': parser.timeSeries()})


app.run(debug = True, port = 3000)