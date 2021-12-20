import pandas as pd
from sklearn.model_selection import train_test_split

min_num_ratings = 5.0
ratings = pd.read_csv("./data/Ratings.csv")
print(ratings.shape)

rating_counts = ratings["User-ID"].value_counts()
keep = rating_counts[rating_counts >= min_num_ratings]

filtered = ratings[ratings["User-ID"].isin(set(keep.index))]
print(filtered.shape)

train, test = train_test_split(
    filtered,
    test_size=0.2,
    random_state=42,
    stratify=filtered['User-ID']
)

print(train.shape)
print(test.shape)

print(len(train["User-ID"].unique()))
print(len(test["User-ID"].unique()))


train.to_csv("./data/ratings_train.csv", index=False)
test.to_csv("./data/ratings_test.csv", index=False)
