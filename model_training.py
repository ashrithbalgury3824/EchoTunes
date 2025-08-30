import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump

# Load the dataset
data = pd.read_csv('songs_with_mood.csv')

# Features and target variable
X = data[['tempo', 'energy', 'valence']]
y = data['mood']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
dump(model, 'music_recommender_model.joblib')
print("Model training complete and saved as 'music_recommender_model.joblib'")
