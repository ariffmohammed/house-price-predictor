# House Price Predictor

A machine learning project that predicts house prices based on size, number of rooms, age, and location score. My first regression project — predicting a continuous number instead of a category.

## How It Works

The model is trained on 20 houses with known prices. Linear Regression learns the relationship between house features and price. Given new house details it predicts an estimated price.

## Example

Input:
- Size: 1500 sq ft
- Rooms: 3
- Age: 5 years
- Location score: 8/10

Output: £358,151

## What I Learned

- Regression vs classification — predicting a number instead of a category
- Linear Regression and how it differs from Logistic Regression
- Working with numerical features instead of text
- Pandas DataFrame as model input

## Tech Stack

- Python
- scikit-learn
- Pandas

## Dataset

20 hardcoded house entries. Full version will use a real world housing dataset such as the Boston Housing or Kaggle House Prices dataset.
