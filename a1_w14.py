'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210428]                                   ##
#*******************************************************************************************#
#############################################################################################
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Class4-Statistics-Week14
# HOMEWORK
# 1)Search the Seaborn Titanic data and write down what the columns mean and 
# what values are they composed of? (data = sns.load_dataset ("titanic"))
# 2)Which are the two columns with the highest correlation in Titanic data?
# 3)For “Fare” columns in Titanic data find

# a) maximum, minimum
# b) mean
# c) mode
# d) median
# f) Draw the graph boxplot

# 4) “penguins” data from Seaborn library (data = sns.load_dataset ("penguins")). Find
# a) How many rows and columns
# b) Find the 2 columns with the highest correlation and draw this in the scatterplot?

# 5) The column "bill_length_mm" of penguins data in Seaborn library, find:
# a) mean
# b) minimum, maximum
# c) mode
# d) median
# e) Draw the graph boxplot

# 6) Find the standard deviations of the columns of penguins data in the Seaborn library and interpret the results?

# Assignment-1 ######################

data=sns.load_dataset('titanic')

print('DATA (titanic) =================================================================')
print(data)

# There are 15 columns:
# 1- Survived: If the passenger survived (0-No, 1-Yes)
# 2- Pclass: Passenger Class (1= First, 2= Second, 3= Third)
# 3- Sex: Male/Female
# 4- Age: Age of the passenger in years
# 5- SibSp: No of sibling/spouses aboard
# 6- Parch: No of parents/chidren aboard
# 7- Fare: Passenger Fare
# 8- Embarked: Port of the embarkatuon (C:Cheboung; Q:Queenstown; S:Southampton)
# 9- class: (First, Second, Third)
# 10- who: man/woman
# 11- adult_male: true/false
# 12- deck: NaN/C
# 13- embark_town: town name
# 14- alive: yes/no
# 15- alone: True/False

# Assignment-2 ######################

print('CORRELATION =================================================================')
print(data.corr())
# The highest correlation is between the columns "sibsp" and "alone" (-0.584471)

# Assignment-3 ######################

print(f"a) max     ---> {data.fare.max()}")
print(f"   min     ---> {data.fare.min()}")
print(f"b) mean    ---> {data.fare.mean()}")
print(f"c) mode    ---> {data.fare.mode()}")
print(f"d) median  ---> {data.fare.median()}")

# e) Boxplot
box = sns.boxplot(x=data["fare"])

print('BOX =================================================================') 
print(box)

# Assignment-4 ######################

data2 = sns.load_dataset ("penguins")

print('DATA2 (penguins) =================================================================')
print(data2)
# a) There are [344 rows and 7 columns]

print('CORRELATION =================================================================')
print(data2.corr())
# b) The highest correlation is between the columns "flipper_length_mm" and "body_mass_g".(0.871202)
# the scatterplot:

scatter = data2.plot.scatter(x='flipper_length_mm', y='body_mass_g', title= "flipper_length_mm & body_mass_g")

print('SCATTER =================================================================')
print(scatter)

# Assignment-5 ######################

print(f"a) max     ---> {data2.bill_length_mm.max()}")
print(f"   min     ---> {data2.bill_length_mm.min()}")
print(f"b) mean    ---> {data2.bill_length_mm.mean()}")
print(f"c) mode    ---> {data2.bill_length_mm.mode()}")
print(f"d) median  ---> {data2.bill_length_mm.median()}")

# e) Boxplot
box2 = sns.boxplot(x=data2["bill_length_mm"])

print('BOX2 =================================================================')
print(box2)

# Assignment-6 ######################

# Find the standard deviations of the columns of penguins data in the Seaborn library and interpret the results?

# If the standard deviation is small, it means the values are scattered close to the average.

standard_deviations = data2.std()

print('STANDARD DEVIATIONS =================================================================')
print(standard_deviations)
