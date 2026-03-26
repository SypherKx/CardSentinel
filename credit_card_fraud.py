import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Loading dataset...")
try:
    credit_card_df = pd.read_csv("creditcard.csv")
except FileNotFoundError:
    print("Error: creditcard.csv not found. Please download the dataset and place it in this directory.")
    exit(1)

# Separate legit and fraud
legit = credit_card_df[credit_card_df.Class == 0]
fraud = credit_card_df[credit_card_df.Class == 1]

print(f"Dataset loaded. Found {len(legit)} legit and {len(fraud)} fraud transactions.")

# Balance dataset dynamically based on fraud count to avoid hardcoding
legit_sample = legit.sample(n=len(fraud), random_state=2)
balanced_df = pd.concat([legit_sample, fraud], axis=0)

# Features & labels
x = balanced_df.drop("Class", axis=1)
y = balanced_df["Class"]

# Train/test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=2
)

print("Training model...")
# Train model
model = LogisticRegression(max_iter=1000, solver="liblinear")
model.fit(x_train, y_train)

# Predictions & accuracy
ypred = model.predict(x_test)
accuracy = accuracy_score(ypred, y_test)
print(f"Model trained! Accuracy: {accuracy:.4f}")

# Save the model
model_filename = 'credit_card_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)
print(f"Model successfully saved to {model_filename}")
