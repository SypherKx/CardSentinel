import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st

# Load dataset
credit_card_df = pd.read_csv("creditcard.csv")

# Balance dataset
legit = credit_card_df[credit_card_df.Class == 0]
fraud = credit_card_df[credit_card_df.Class == 1]

legit_sample = legit.sample(n=len(fraud), random_state=2)
credit_card_df = pd.concat([legit_sample, fraud], axis=0)

# Features & labels
x = credit_card_df.drop("Class", axis=1)
y = credit_card_df["Class"]

# Train/test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=2
)

# Train model
model = LogisticRegression(max_iter=1000, solver="liblinear")
model.fit(x_train, y_train)

train_acc = accuracy_score(model.predict(x_train), y_train)
test_acc = accuracy_score(model.predict(x_test), y_test)

# ---------------- Streamlit UI ----------------
st.title("💳 Credit Card Fraud Detection Model")
st.write(f"✅ Training Accuracy: {train_acc:.2%}")
st.write(f"✅ Testing Accuracy: {test_acc:.2%}")

st.subheader("🔍 Try a Transaction:")

# User input
input_df = st.text_input("Enter all required feature values (comma separated):")

if st.button("Submit"):
    try:
        input_df_splited = [val.strip() for val in input_df.split(",")]
        
        if len(input_df_splited) != x.shape[1]:
            st.error(f"⚠️ You must enter exactly {x.shape[1]} values (Time, V1...V28, Amount).")
        else:
            features = np.asarray(input_df_splited, dtype=np.float64).reshape(1, -1)
            prediction = model.predict(features)
            if prediction[0] == 0:
                st.success("✅ The transaction is Legit")
            else:
                st.error("🚨 The transaction is Fraud")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

#to run this type------ 
#cd "D:\Downloads\Credit Card website"
#python -m streamlit run website.py
