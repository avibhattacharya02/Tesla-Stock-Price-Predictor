#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb 

from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model import LogisticRegression 
from sklearn.svm import SVC  
from sklearn import metrics
import warnings 
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('C:\\Users\\sidhu\\Downloads\\TeslaStockPrice.csv') 
print(df.head())
print(df.shape)

# Describe and info
print(df.describe())
print(df.info())

# Plotting the Close price
plt.figure(figsize=(15,5)) 
plt.plot(df['Close']) 
plt.title('Tesla Close price', fontsize=18) 
plt.ylabel('Price in dollars') 
plt.show()

# Checking for null values
print(df.isnull().sum())

# Plotting distributions
features = ['Open', 'High', 'Low', 'Close', 'Volume'] 

plt.subplots(figsize=(20,10)) 

for i, col in enumerate(features): 
    plt.subplot(2,3,i+1) 
    sb.histplot(df[col], kde=True) 
plt.show()

# Plotting boxplots
plt.subplots(figsize=(20,10)) 
for i, col in enumerate(features): 
    plt.subplot(2,3,i+1) 
    sb.boxplot(df[col]) 
plt.show()

# Extract year from Date column
df['Date'] = pd.to_datetime(df['Date'])
df['year'] = df['Date'].dt.year

# Group by year and plot
data_grouped = df.groupby('year').mean() 
plt.subplots(figsize=(20,10)) 

for i, col in enumerate(['Open', 'High', 'Low', 'Close']): 
    plt.subplot(2,2,i+1) 
    data_grouped[col].plot.bar() 
    plt.title(f'Average {col} by Year')
plt.show()


# In[ ]:




