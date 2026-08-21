import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data/training_dataset.csv")

X = df.drop("HiringScore", axis=1)
y = df["HiringScore"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(

    n_estimators=200,

    random_state=42

)

model.fit(X_train, y_train)

joblib.dump(

    model,

    "models/random_forest.pkl"

)

print("Random Forest Saved")