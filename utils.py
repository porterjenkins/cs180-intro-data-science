from sklearn.model_selection import train_test_split


def split_write(df, name, test_size, y_name):

    y = df[y_name]
    X = df.drop(y_name, axis='columns')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    y_train = y_train.to_frame(name=y_name)
    y_test = y_test.to_frame(name=y_name)


    X_train.to_csv(f"./data/{name}_x_train.csv", index=False)
    X_test.to_csv(f"./data/{name}_x_test.csv", index=False)

    y_train.to_csv(f"./data/{name}_y_train.csv", index=False)
    y_test.to_csv(f"./data/{name}_y_test.csv", index=False)
