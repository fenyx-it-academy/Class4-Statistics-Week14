#!/usr/bin/env python
# coding: utf-8

# # Class4-Statistics-Week14
# HOMEWORK

# # Question 1)
# Search the Seaborn Titanic data and write down what the columns mean and what values are they composed of? (data = sns.load_dataset ("titanic"))

# # Solution 1: Titanic Dataset –
# It is one of the most popular datasets used for understanding machine learning basics. It contains information of all the passengers aboard the RMS Titanic, which unfortunately was shipwrecked. This dataset can be used to predict whether a given passenger survived or not.
# The csv file can be downloaded from Kaggle.
# The columns:
# 1- PassengerId: Unique ID of a passenger.
# 2- Survived: If the passenger survived (0-No, 1-Yes)
# 3- Pclass: Passenger Class (1= First, 2= Second, 3= Third)
# 4- Name: Name of the passenger
# 5- Sex: Male/Female
# 6- Age: Age of the passenger in years
# 7- SibSp: No of sibling/spouses aboard
# 8- Parch: No of parents/chidren aboard
# 9- Ticket: Ticket Number
# 10- Fare: Passenger Fare
# 11- Cabin: Cabin Nummber
# 12- Embarked: Port of the embarkatuon (C:Cheboung; Q:Queenstown; S:Southampton)
# 

# In[1]:


import seaborn as sns

df_titanic=sns.load_dataset("titanic")
df_titanic


# # Question 2)
# Which are the two columns with the highest correlation in Titanic data?

# In[2]:


df_titanic.corr()

### The highest correlation is between the columns "sibsp" and "alone" (0.584471).###


# # Question 3)
# For “Fare” columns in Titanic data find
# a) maximum, minimum
# b) mean
# c) mode
# d) median
# and
# f) Draw the graph boxplot

# In[21]:


import pandas as pd
import numpy as np

# a) Maximum and minimum for "fare" column:
print("--Maximum fare: {}". format (df_titanic.fare.max()))
print("--Minimum fare: {}". format (df_titanic.fare.min()))

# b) mean
print("--Mean of fare : {}".format(df_titanic.fare.mean()))

# c) mode
print("--Mode of fare : {}".format(df_titanic.fare.mode()))

# d) median
print("--Median of fare : {}".format(df_titanic.fare.median()))

# e) Boxplot
sns.boxplot(x=df_titanic["fare"])


# # Question 4)
# “penguins” data from Seaborn library (data = sns.load_dataset ("penguins")). Find
# a) How many rows and columns
# b) Find the 2 columns with the highest correlation and draw this in the scatterplot?

# In[33]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plot

df_pen = sns.load_dataset("penguins")

# a) 344 rows and 7 colomns

# b) 
df_pen.corr()
### The highest correlation is between the columns "flipper_length_mm" and "body_mass_g".(0.871202) ###

# Draw a scatter plot

df_pen.plot.scatter(x='flipper_length_mm', y='body_mass_g', title= "Scatter plot between two variables flipper_length_mm and body_mass_g");

plot.show(block=True);


# # Question 5)
# The column "bill_length_mm" of penguins data in Seaborn library, find:
# a) mean
# b) minimum, maximum
# c) mode
# d) median
# e) Draw the graph boxplot

# In[36]:


import pandas as pd
import numpy as np

# b) mean
print("--Mean of bill_length_mm : {}".format(df_pen.bill_length_mm.mean()))

# a) Maximum and minimum for "bill_length_mm" column:
print("--Maximum bill_length_mm: {}". format (df_pen.bill_length_mm.max()))
print("--Minimum bill_length_mm: {}". format (df_pen.bill_length_mm.min()))

# c) mode
print("--Mode of bill_length_mm : {}".format(df_pen.bill_length_mm.mode()))

# d) median
print("--Median of bill_length_mm : {}".format(df_pen.bill_length_mm.median()))

# e) Boxplot
sns.boxplot(x=df_pen["bill_length_mm"])


# # Question 6)
# Find the standard deviations of the columns of penguins data in the Seaborn library and interpret the results?

# In[44]:


import pandas as pd

answer= df_pen.std()
print("The standard deviations of the columns of the Penguins database:")
print (answer)

""" The standart deviation of the column "body_mass_g" is so high. This indicates that 
the differences between the values are too high.

The standart deviation of the column "bill_depth_mm" is not so high. 
So, the values are closer to each others then another columns.     """       

