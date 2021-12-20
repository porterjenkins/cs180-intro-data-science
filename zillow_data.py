import pandas as pd
from utils import split_write

fpaths = [
    "/home/porter/Documents/teaching/cs180/code/cs180-intro-data-science/data/chicago_zillow_house_price.csv",
    "/home/porter/Documents/teaching/cs180/code/cs180-intro-data-science/data/nyc_zillow_house_price_big.csv"
]

y_col = "priceSqft"

dfs = []
for f in fpaths:
    city_df = pd.read_csv(f)
    dfs.append(city_df)

data = pd.concat(dfs, axis=0)

split_write(data, name='zillow', test_size=0.2, y_name=y_col)
