#Loading dataset from a csv format using Pandas
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.naive_bayes import GaussianNB

from sklearn.feature_extraction.text import TfidfTransformer


from sklearn.metrics import accuracy_score

filename = 'Trou aux Biches Beachcomber Golf Resort & Spa.csv'
filename1 = 'Clean_1.csv'

train_dataset = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\correct_equal_combined.csv'
test_dataset = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\test_correct_300_each.csv'

#names =['CT','CS','C','D','M','R']

hotel = pd.read_csv(train_dataset, encoding='latin-1')
hotel_test = pd.read_csv(test_dataset, encoding='latin-1')

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

# X_train, X_test, y_train, y_test = train_test_split(hotel, hotel.Rating, test_size=0.5, shuffle=False)
X_train = hotel
y_train = hotel.Rating

X_test = hotel_test
y_test = hotel_test.Rating

print(hotel.shape)
print(X_train.shape)
print(y_train.shape)


count = CountVectorizer(stop_words='english', tokenizer=None, ngram_range=(1, 2), min_df=50, max_df=0.9)
temp = count.fit_transform(X_train['Comment'].values.astype('str'))  # word count for recurrent words

print(count.get_feature_names())

#print("temp: " + temp)

tdif = TfidfTransformer(norm='l2')
temp2 = tdif.fit_transform(temp) # Give words different Weights

print(tdif)

text_regression = LogisticRegression()

model = text_regression.fit(temp2, y_train)

prediction_data = tdif.transform(count.transform(X_test['Comment'].values.astype('str')))

predicted = model.predict(prediction_data)

# for c, d in zip(predicted, y_test):
#     print(c, d)
print(np.mean(predicted == y_test))

print(accuracy_score(y_test,predicted))

print("Printing how many was correct: ")
print(accuracy_score(y_test,predicted, normalize=False))


print("\n\n\n Printing for custom sentence: ")
print(model.predict(tdif.transform(count.transform(["The hotel was beautiful but the food was not good"]))))