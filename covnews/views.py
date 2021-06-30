from django.shortcuts import render
from newsapi import NewsApiClient
import pandas as pd
import plotly.express as px

newsapi = NewsApiClient(api_key='1d537670596e4a10b01e51e0c3824cea')
# Create your views here.


def news(request):

    df = pd.read_csv(
        "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='Reds'
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=500, margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.write_html("templates/map.html", full_html=False,
                   include_plotlyjs='cdn')
    all_articles = newsapi.get_everything(q='corona india',
                                          language='en',
                                          sort_by='relevancy',
                                          page=2)
    cov = {'covnews': all_articles["articles"]}
    return render(request, 'covnews/newslist.html', cov)
