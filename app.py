from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model on server startup instead of per-request
try:
    with open('credit_card_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    model = None
    print(f"Warning: Could not load credit_card_model.pkl ({e}). Please run credit_card_fraud.py first.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Prediction model is missing. Please contact administrator.'}), 500
        
    try:
        data = request.json.get('features', '')
        if not data:
            return jsonify({'error': 'No input data provided.'}), 400
            
        # Parse the comma-separated input string
        features_list = [val.strip() for val in data.split(',')]
        
        if len(features_list) != 30:
            return jsonify({'error': f'Invalid input length. Expected 30 comma-separated numeric features (Time, V1-V28, Amount), got {len(features_list)}.'}), 400
            
        features_array = np.asarray(features_list, dtype=np.float64).reshape(1, -1)
        
        # Predict: 0 = Legit, 1 = Fraud
        prediction = model.predict(features_array)
        
        if prediction[0] == 0:
            return jsonify({'status': 'legit'})
        else:
            return jsonify({'status': 'fraud'})

    except ValueError:
        return jsonify({'error': 'Invalid numeric value. Ensure all 30 features are numbers.'}), 400
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    print("Starting Card Sentinel web server...")
    app.run(debug=True, port=5000)
