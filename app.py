import os

from dash import Dash, dcc, html, Input, Output
import pandas as pd

from functions import load_df


DATA_FOLDER = os.path.abspath('data')
DATASET_FILE = os.path.join(DATA_FOLDER, 'TA_restaurants_curated.csv')
PROCESSED_DATA_FOLDER = os.path.join(DATA_FOLDER, 'processed')

CITIES_FILE = os.path.join(PROCESSED_DATA_FOLDER, 'cities.csv')
STYLES_FILE = os.path.join(PROCESSED_DATA_FOLDER, 'cuisine_styles.csv')
CITIES_STYLES_FILE = os.path.join(PROCESSED_DATA_FOLDER, 'city_cuisine_styles.csv')

TITLE = 'Restaurant Dashboard'

external_stylesheets = [
    {
        'rel': 'stylesheet', 
        'href': 'https://cdn.jsdelivr.net/gh/jgthms/minireset.css@master/minireset.min.css'
    },
]


def main():

    # load the DataFrames
    CITIES_DF = load_df(CITIES_FILE)
    STYLES_DF = load_df(STYLES_FILE)
    CITIES_STYLES_DF = load_df(CITIES_STYLES_FILE)

    DISTINCT_CITIES = CITIES_DF['city_name'].unique()
    DISTINCT_STYLES = STYLES_DF['style_name'].unique()


    app = Dash(__name__, external_stylesheets=external_stylesheets)
    app.title = TITLE

    app.layout = html.Main(
        children = [
            html.Header(children=html.H1(children=TITLE)), 
            html.Div(
                id='menu', 
                children=[     
                    html.H2(children='Cities'), 
                    dcc.Dropdown(
                        id='city-quick-filter', 
                        className='single-dropdown', 
                        options=[
                            {'label': city, 'value': city} 
                            for city in [
                                'All', 'Top 3', 'Top 5', 'Top 10', 
                                'Most Popular', 'Most Restaurants', 
                                'Highest Rated', 'Most Rated', 'Most Reviewed', 
                                'Least Popular', 'Least Rated'
                            ]
                        ], 
                        value='Highest Rated', 
                        clearable=False, 
                    ), 
                    dcc.Dropdown(
                        id='city-filter', 
                        className='multi-dropdown', 
                        options=[
                            {'label': city, 'value': city} 
                            for city in DISTINCT_CITIES
                        ], 
                        #value='ALL', 
                        placeholder='Select a city', 
                        multi=True, 
                        clearable=False, 
                    ), 
                    html.Div(id='city-filter-output'), 
                    html.Br(), 
                    html.H2(children='Cuisine Styles'), 
                    dcc.Dropdown(
                        id='style-quick-filter', 
                        className='single-dropdown', 
                        options=[
                            {'label': style, 'value': style} 
                            for style in [
                                'All', 
                                'Most Common', 'Most Popular', 
                                'Most Reviewed', 'Highest Rated', 
                                'Least Common', 'Least Popular', 
                                'Least Reviewed', 'Lowest Rated', 
                            ]
                        ], 
                        value='Most Popular', 
                        clearable=False, 
                    ), 
                    dcc.Dropdown(
                        id='style-filter', 
                        className='multi-dropdown', 
                        options=[
                            {'label': style, 'value': style} 
                            for style in DISTINCT_STYLES
                        ], 
                        placeholder='Select a cuisine style', 
                        multi=True, 
                        clearable=False, 
                    )
                ]
            ), 
            html.Div(
                id='graphs', 
                children=[]
            ), 
        ]
    )

    @app.callback(
        Output('city-filter-output', 'children'),
        Input('city-filter', 'value')
    )
    def update_output(value):
        #return f'You have selected {value}'
        pass

    app.run_server(debug=True)


if __name__ == '__main__':
    main()
