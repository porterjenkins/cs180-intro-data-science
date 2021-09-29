import pandas as pd
from sklearn.model_selection import train_test_split


def split_write(df, test_size, y_name):

    y = df[y_name]
    X = df.drop(y_name, axis='columns')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    y_train = y_train.to_frame(name=y_name)
    y_test = y_test.to_frame(name=y_name)


    X_train.to_csv("./data/zillow_x_train.csv", index=False)
    X_test.to_csv("./data/zillow_x_test.csv", index=False)

    y_train.to_csv("./data/zillow_y_train.csv", index=False)
    y_test.to_csv("./data/zillow_y_test.csv", index=False)


fpaths = [
    "/home/porter/Documents/teaching/cs180/code/cs180-intro-data-science/data/chicago_zillow_house_price.csv",
    "/home/porter/Documents/teaching/cs180/code/cs180-intro-data-science/data/nyc_zillow_house_price_big.csv"
]

y_col = "sqft"

dfs = []
for f in fpaths:
    city_df = pd.read_csv(f)
    dfs.append(city_df)

data = pd.concat(dfs, axis=0)

split_write(data, test_size=0.2, y_name=y_col)
