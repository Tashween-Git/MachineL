#Loading dataset from a csv format using Pandas
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.naive_bayes import GaussianNB

from sklearn.feature_extraction.text import TfidfTransformer

filename = 'Trou aux Biches Beachcomber Golf Resort & Spa.csv'
filename1 = 'Clean_1.csv'


#names =['CT','CS','C','D','M','R']

hotel = pd.read_csv(filename1)

print(hotel.head())

print(hotel.info())

print(hotel.describe())

print(hotel.columns)

# print(hotel._ix[5,15,20])

# print(hotel['Comments', 'Rating'])

print("Hello :")
print(hotel.groupby("Rating").Countries.describe())


for x in hotel:
    print(x)
# Starting the process

X_train, X_test, y_train, y_test = train_test_split(hotel, hotel.Rating, test_size=0.5, shuffle=False)


print(hotel.shape)
print(X_train.shape)
print(y_train.shape)


count = CountVectorizer()
temp = count.fit_transform(X_train['Comments'].values.astype('str'))  # word count for recurrent words


#print("temp: " + temp)

tdif = TfidfTransformer()
temp2 = tdif.fit_transform(temp) # Give words different Weights

# text_regression = LogisticRegression()
text_regression = GaussianNB()

model = text_regression.fit(temp2, y_train)

prediction_data = tdif.transform(count.transform(X_test['Comments'].values.astype('str')))

predicted = model.predict(prediction_data)

for c, d in zip(predicted, y_test):
    print(c, d)
print(np.mean(predicted == y_test))


print("\n\n\n Printing for custom sentence: ")
print(model.predict(tdif.transform(count.transform(["not outstanding but quite nice with tasty food and good bed"]))))