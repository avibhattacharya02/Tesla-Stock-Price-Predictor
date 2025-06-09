Tesla Stock Price Analysis

This project involves analyzing Tesla's stock prices using Python. The analysis includes data preprocessing, exploratory data analysis (EDA), and visualizations to better understand the trends and behaviors of Tesla's stock over time.

Introduction

The goal of this project is to delve into Tesla's stock prices and uncover trends and patterns. We will use various Python libraries to manipulate the data, create visualizations, and perform some machine learning tasks.

Data

The dataset used in this project is TeslaStockPrice.csv, which includes the following columns:

Date: The date of the stock price record.
Open: The opening price of the stock.
High: The highest price of the stock during the day.
Low: The lowest price of the stock during the day.
Close: The closing price of the stock.
Volume: The volume of shares traded.
Installation

To run this project, you need Python installed on your system along with several libraries. You can install these libraries using pip. Here are the required libraries:

numpy
pandas
matplotlib
seaborn
scikit-learn
You can install them by running the following command:

sh
Copy code
pip install numpy pandas matplotlib seaborn scikit-learn
Usage

Download or clone the project repository.
Ensure the TeslaStockPrice.csv file is in the same directory as the Python script.
Run the script in a Python environment by executing:
sh
Copy code
python tesla_stock_analysis.py
Project Structure

The project contains the following files:

tesla_stock_analysis.py: 🧠 Model Performance Summary
This project compares the performance of three machine learning models for classification tasks: Logistic Regression, Support Vector Classifier (SVC) with a polynomial kernel, and XGBoost Classifier.

📊 Results:
Model	Training Accuracy	Validation Accuracy
Logistic Regression	0.5192	0.5435
SVC (Polynomial Kernel)	0.4717	0.4468
XGBoost Classifier	0.9645	0.5730

🔍 Observations:
XGBoost performed the best overall but showed signs of overfitting (high training accuracy vs. validation).

Logistic Regression provided more balanced performance and may generalize better on unseen data.

SVC with polynomial kernel underperformed and may not be suitable for this dataset.
