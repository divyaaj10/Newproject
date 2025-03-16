import pickle
import os
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Create the saved_models folder if it doesn't exist
model_dir = "saved_models"
os.makedirs(model_dir, exist_ok=True)

# Dummy training data (replace with actual datasets)
X_train = np.random.rand(100, 8)
y_train = np.random.randint(2, size=100)

# Train and save Diabetes Model
diabetes_model = RandomForestClassifier()
diabetes_model.fit(X_train, y_train)
pickle.dump(diabetes_model, open(os.path.join(model_dir, "diabetes_model.sav"), "wb"))

# Train and save Heart Disease Model
heart_disease_model = RandomForestClassifier()
heart_disease_model.fit(X_train, y_train)
pickle.dump(heart_disease_model, open(os.path.join(model_dir, "heart_disease_model.sav"), "wb"))

# Train and save Parkinson’s Model
parkinsons_model = RandomForestClassifier()
parkinsons_model.fit(X_train, y_train)
pickle.dump(parkinsons_model, open(os.path.join(model_dir, "parkinsons_model.sav"), "wb"))

print("✅ All models trained and saved in 'saved_models' directory.")
