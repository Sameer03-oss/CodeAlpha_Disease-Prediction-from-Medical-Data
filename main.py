from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Disease Prediction Model")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Predict using a sample from the dataset
sample = X_test[0].reshape(1, -1)
result = model.predict(sample)[0]

if result == 0:
    print("Prediction: Malignant")
else:
    print("Prediction: Benign")