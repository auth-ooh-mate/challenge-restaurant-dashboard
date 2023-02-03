import os
import pandas as pd


def load_df(file):

    if not os.path.exists(file): 
        print('File doesn\'t exist:', file)
        return

    else: return pd.read_csv(file)


def filter_df(**kwargs):
    pass

def top_cities(n=10):
    pass

def top_styles(n=10):
    pass

def top_rated_cities(n=10):
    pass

def most_rated_cities(n=10):
    pass

def top_reviewed_cities(n=10):
    pass

def most_reviewed_cities(n=10):
    pass

def most_common_cuisine_styles(city='ALL', n=10):
    pass

def least_common_cuisine_styles(city='ALL', n=10):
    pass

def top_rated_cuisine_styles(city='ALL', n=10):
    pass

def most_rated_cuisine_styles(city='ALL', n=10):
    pass
