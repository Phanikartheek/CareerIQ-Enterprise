import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import joblib

# Load Dataset
df = pd.read_csv("data/training_dataset.csv")

X = df.drop("HiringScore", axis=1)
y = df["HiringScore"]

# Scale Features
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Save scaler
joblib.dump(scaler, "models/scaler.pkl")

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Build Neural Network
model = Sequential()

model.add(Dense(32, activation="relu", input_shape=(7,)))
model.add(Dense(16, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

model.fit(
    X_train,
    y_train,
    epochs=150,
    batch_size=4,
    validation_split=0.2,
    verbose=1
)

model.save("models/deep_learning_model.keras")

print("Deep Learning Model Saved Successfully")