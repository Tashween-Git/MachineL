#Loading dataset from a csv format using Pandas

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

filename = 'Trou aux Biches Beachcomber Golf Resort & Spa.csv'

#names =['CT','CS','C','D','M','R']

hotel = pd.read_csv(filename)

print(hotel.head())

print(hotel.info())

print(hotel.describe())

print(hotel.columns)

# print(hotel._ix[5,15,20])

# print(hotel['Comments', 'Rating'])

print("Hello :")
print(hotel.groupby("Rating").Countries.describe())