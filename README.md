# Disease Prediction from Medical Data

## Objective
To predict disease categories using machine learning and structured medical data.

## Description
This project uses Logistic Regression to classify breast cancer data into two categories: Malignant and Benign.

The model is trained using a dataset provided by Scikit-learn.

## Features
- Loads a medical dataset.
- Splits data into training and testing sets.
- Trains a Logistic Regression model.
- Calculates model accuracy.
- Predicts the category of a sample record.

## Technologies Used
- Python
- Scikit-learn
- Machine Learning
- Logistic Regression

## Dataset
The project uses the built-in Breast Cancer Wisconsin dataset available in Scikit-learn. No manual dataset download is required.

## Installation

Install the required library:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Execute the following command:

```bash
python main.py
```

## Expected Output

```text
Disease Prediction Model
Model Accuracy: (depends on the model)
Prediction: Malignant or Benign
```

The actual accuracy and prediction will be displayed when the program runs.

## Algorithm
Logistic Regression is used to classify the medical data into two categories.

## Future Improvements
- Add heart disease prediction.
- Add diabetes prediction.
- Implement Random Forest and SVM.
- Create a graphical user interface.
- Improve model evaluation.

## Disclaimer
This project is intended for educational purposes only. It is not a medical diagnostic tool and must not be used to make healthcare decisions.
