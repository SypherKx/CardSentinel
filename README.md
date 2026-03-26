# 🛡️ CardSentinel | AI Fraud Detection System

CardSentinel is a professional-grade machine learning application designed to detect fraudulent credit card transactions in real-time. It features a high-performance **Logistic Regression** model and a stunning, modern **Flask-based Web UI**.

![Screenshot](/api/placeholder/800/400) <!-- You can add a real screenshot here later! -->

## ✨ Features
- **Real-time Detection**: Analyze transactions instantly using a pre-trained ML model.
- **Premium UI**: Modern dark-mode interface with Glassmorphism, tailored animations, and Lucide icons.
- **Efficient Backend**: Built with Flask, loading the model into memory for lightning-fast predictions.
- **Automated Balancing**: Dynamically handles imbalanced datasets for better accuracy.

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-Learn, Pandas, NumPy, Pickle
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+), Lucide Icons

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SypherKx/CardSentinel.git
   cd CardSentinel
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get the Dataset**:
   Download the **[Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)** from Kaggle and place `creditcard.csv` in the root directory.

4. **Train the Model** (One-time):
   ```bash
   python credit_card_fraud.py
   ```

## 🚀 Running the App

Start the Flask server:
```bash
python app.py
```
Open your browser and navigate to: `http://127.0.0.1:5000`

## 📊 How it Works
CardSentinel uses a **Logistic Regression** classifier trained on a balanced subset of transactions. Because the original dataset is highly skewed (very few frauds), the script automatically samples legitimate transactions to match the number of fraud cases. This ensures the model learns the "patterns of fraud" effectively without bias.

---
Developed by **SypherKx** &bull; 2026
