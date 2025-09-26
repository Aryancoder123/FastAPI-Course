from sklearn.linear_model import LinearRegression
import joblib
import pandas as pd

data = pd.read_csv("housing.csv").iloc[:, :-1].dropna()

X = data.drop(columns=["median_house_value"])
Y = data.median_house_value.copy()

model = LinearRegression()
trained_model = model.fit(X, Y)

joblib.dump(trained_model, "model.joblib")
