from core.ml_prediction import MLPredictor

ml = MLPredictor()

print("Training models...")

result = ml.train_models()

print(result)

print("Models saved successfully.")