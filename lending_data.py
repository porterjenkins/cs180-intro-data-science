import pandas as pd
from utils import split_write

fpath = "/home/porter/Documents/teaching/cs180/code/cs180-intro-data-science/data/loan_data.csv"

rename = {'credit.policy': 'is.approved'}

y_col = 'is.approved'

df = pd.read_csv(fpath)
df.rename(columns=rename, inplace=True)
print(df.head())

split_write(df, name='loan',test_size=0.2, y_name=y_col)
