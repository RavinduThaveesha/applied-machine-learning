import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from sklearn import preprocessing

#load data from csv
df = pd.read_csv('data.csv')
df.head()

#check how many of each class is in our data set
df['custcat'].value_counts()

#data vizualization
df.hist(column='income', bins=50)

#let's define feature set
df.columns

#to use scikit-learn library, we have to convert the Pandas data frame to a Numpy array
x = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']].values  #.astype(float)
x[0:5]

y = df['custcat'].values
y[0:5]





