import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib

df = pd.read_csv('data/desafio_indicium.csv')
X = df.drop(columns=['IMDB_Rating'])
y = df['IMDB_Rating']

numeric_features = ['Released_Year', 'Runtime', 'Meta_score', 'Gross', 'No_of_Votes']
categorical_features = ['Certificate', 'Genre']

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(), categorical_features)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', Ridge())
])

pipeline.fit(X, y)
joblib.dump(pipeline, 'models/imdb_model.pkl')
