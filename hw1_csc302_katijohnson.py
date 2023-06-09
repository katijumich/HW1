# -*- coding: utf-8 -*-
"""HW1_CSC302_KatiJohnson.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WEkkM3T4QJWo6hpgP_ibZg2sq5Jc06jx
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import csv

with open("/content/drive/MyDrive/CSC302/DATA/olympic_medals.csv") as f:
    reader = csv.DictReader(f)
    olympics_data = list(reader)

"""Set the olympics data as the dataframe"""

df = pd.DataFrame(olympics_data)
df.head()

"""**A**"""

df.info()

print("Number of rows:",len(df))
print("Number of columns:",len(df.columns))

"""**B**"""

df.dtypes

"""**C**"""

print("There are",len(df['Location'].unique()),"unique cities where matches were held.")

"""**D**"""

print("The USA has won",len(df.loc[df['Nationality'] == "USA"]),"medals.")

"""**E**"""

df.groupby(by='Nationality')['Medal'].count()