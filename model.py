import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("stress.csv")

# Encode labels
le = LabelEncoder()
data['stress'] = le.fit_transform(data['stress'])

# Features
X = data[['sleep', 'screen', 'work', 'mood', 'activity']]
y = data['stress']

# Train model
model = DecisionTreeClassifier(max_depth=4)
model.fit(X, y)

# Function for prediction
def predict_stress(input_data):
    pred = model.predict([input_data])
    return le.inverse_transform(pred)[0]