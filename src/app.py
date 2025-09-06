from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)
model = joblib.load(r'C:\Users\sarav\OneDrive\Área de Trabalho\Trabalhos\LightHouse\LH_CD_SARA\models\imdb_model.pkl')

@app.route('/model/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Campos esperados pelo modelo
    expected_fields = ['Released_Year', 'Runtime', 'Meta_score', 'Gross', 'No_of_Votes', 'Certificate', 'Genre', 'Cleaned_Overview']
    # Filtra e converte os campos
    input_data = {}
    for field in expected_fields:
        if field == 'Cleaned_Overview':
            # Usa o valor de Overview_clean enviado pelo frontend
            value = data.get('Overview_clean', '')
            input_data[field] = value
        else:
            value = data.get(field, None)
            if field in ['Released_Year', 'Runtime', 'Meta_score', 'Gross', 'No_of_Votes']:
                try:
                    input_data[field] = float(value) if value is not None and value != '' else 0.0
                except Exception:
                    input_data[field] = 0.0
            else:
                input_data[field] = value if value is not None else ''
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return jsonify({'predicted_rating': round(prediction, 2)})

@app.route('/eda/summary', methods=['GET'])
def eda_summary():
    df = pd.read_csv('data/desafio_indicium.csv')
    summary = df.describe(include='all').to_dict()
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)
