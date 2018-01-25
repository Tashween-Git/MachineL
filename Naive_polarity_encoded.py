#Loading dataset from a csv format using Pandas
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.naive_bayes import GaussianNB, MultinomialNB

from sklearn.feature_extraction.text import TfidfTransformer

# For preprocessing the data
from sklearn.preprocessing import Imputer
from sklearn import preprocessing

# To calculate the accuracy score of the model
from sklearn.metrics import accuracy_score

filename = 'Trou aux Biches Beachcomber Golf Resort & Spa.csv'
filename1 = 'Clean_1.csv'

train_dataset = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\correct_equal_combined_pos_neg_no_3.csv'
test_dataset = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\test_correct_300_each_pos_neg_no_3.csv'

#names =['CT','CS','C','D','M','R']

# hotel = pd.read_csv(filename1)

hotel = pd.read_csv(train_dataset, encoding='latin-1')
hotel_test = pd.read_csv(test_dataset, encoding='latin-1')

print("head(): \n")
print(hotel.head())

print("info(): \n")

print(hotel.info())

print("describe(): \n")

print(hotel.describe())

print("columns(): \n")

print(hotel.columns)

# print(hotel._ix[5,15,20])

# print(hotel['Comments', 'Rating'])

print("1. Handling missing data(): \n")
print("Checking null(): \n")
print(hotel.isnull().sum())  # Handling missing data

print("checking for '?' presence: \n")
# for value in hotel.columns:
#     print(value, ":", sum(hotel[value] == '?'))

hotel_dup = hotel  # duplicating before pre processing

# Performing Imputation
print("2. Performing Imputation: \n")

# summary of all attributes in the dataset
print("hotel_dup summary for all attributes(): \n")
print(hotel_dup.describe(include='all'))

X_train = hotel
y_train = hotel.Polarity

X_test = hotel_test
y_test = hotel_test.Rating

y_test = hotel_test.Polarity


print(hotel.shape)
print(X_train.shape)
print(y_train.shape)


count = CountVectorizer(stop_words='english', tokenizer=None, ngram_range=(1, 2), min_df=1, max_df=0.9)
temp = count.fit_transform(X_train['Comment'].values.astype('str'))  # word count for recurrent words

print(count.get_feature_names())

print("Stop Words:")
print(count.get_stop_words())
print(temp.shape)
#print("temp: " + temp)

tdif = TfidfTransformer(norm='l1')
temp2 = tdif.fit_transform(temp) # Give words different Weights

#print(temp2)

# nb = GaussianNB()
mn = MultinomialNB()

# Must convert to dense matrix for GaussianNB
# X = temp2.todense()
# nb.fit(X, hotel['Rating'])

#mn.fit(temp2, hotel['Rating'])

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
le.fit(["Positive", "Negative"])

y = le.transform(y_train)
mn.fit(temp2, y)


prediction_data = tdif.transform(count.transform(X_test['Comment'].values.astype('str')))

predicted = mn.predict(prediction_data)

pos=0
neg=0
net=0
wrong =0

# for c, d in zip(predicted, y_test):
#     print(c, d)
#     if ((c > 3) & (d > 3)):
#         pos = pos+1
#     elif ((c < 3) & (d < 3)):
#         neg = neg+1
#     elif ((c == 3) & (d == 3)):
#         net = net+1
#     else:
#         wrong = wrong +1
#
#     print("Accuracy for polarity is: " + str(((pos/600)+(neg/600)+(net/300))/3))
#     print("Wrong classification: " + str(wrong))


print(np.mean(predicted == le.transform(y_test)))

# print(nb.predict(tfidf_transformer.transform(vectorizer.transform(["Very disappointing and bad, didn't expect such crap service"])).todense()))
# print(mn.predict(tfidf_transformer.transform(vectorizer.transform(["Very disappointing and bad, didn't expect such crap service"])).todense()))
#
# print(nb.predict(tfidf_transformer.transform(vectorizer.transform(["We went to Mauritius and Dubai to celebrate our 10th Wedding Anniversary and stayed at Port Chambly when we were in Mauritius. We had done a swap through Interval International and had been allocated a 1 bedroom appartment| but when we checked in we were given a 3 bedroom which was nice| and we were able to check in 4 1/2 hours which was excellent. The apartment was excellently laid out and furnished and the main bed was very big and comfy. There was free WiFi in the bar area| and we were presented with a complimentary cocktail on arrival| which was a nice touch.That was the really very good bits. On the negative side the resort is extremely isolated and quite dificult to find from the main motorway from the airport for the first time. We like to be able to walk to local restaurants from where we are staying and this was absolutely impossible here. You needed a car to get anywhere though there was a bus stop outside the main entrance we didn't try public transport. The onsite restaurant and bar was very expensive compared to the restaurants we travelled out to| and the staff were not veery knowledgeable on tours available to be booked. There was only 1 English channel on the satellite receiver and that was BBC World News.With a car we found the resort well situated to tour the island once we'd worked out the back roads and short cuts| and didn'tr find too many problems getting into Port Louis by road| despite some previous comments on Trip Advisor| though it was busy during the rush hour but this would apply to any hotel / resort in the Port Louis area unless you were staying at Caudan Waterfront.If you do come to Port Chambly and want to stock up the kitchen we'd recommend going a few miles to the South African supermarkets (Pick'n'Pay| Intermart & Food Lovers Paradise) at Grand Baie rather than the nearby Jumbo supermarket."])).todense()))
# print(mn.predict(tfidf_transformer.transform(vectorizer.transform(["We went to Mauritius and Dubai to celebrate our 10th Wedding Anniversary and stayed at Port Chambly when we were in Mauritius. We had done a swap through Interval International and had been allocated a 1 bedroom appartment| but when we checked in we were given a 3 bedroom which was nice| and we were able to check in 4 1/2 hours which was excellent. The apartment was excellently laid out and furnished and the main bed was very big and comfy. There was free WiFi in the bar area| and we were presented with a complimentary cocktail on arrival| which was a nice touch.That was the really very good bits. On the negative side the resort is extremely isolated and quite dificult to find from the main motorway from the airport for the first time. We like to be able to walk to local restaurants from where we are staying and this was absolutely impossible here. You needed a car to get anywhere though there was a bus stop outside the main entrance we didn't try public transport. The onsite restaurant and bar was very expensive compared to the restaurants we travelled out to| and the staff were not veery knowledgeable on tours available to be booked. There was only 1 English channel on the satellite receiver and that was BBC World News.With a car we found the resort well situated to tour the island once we'd worked out the back roads and short cuts| and didn'tr find too many problems getting into Port Louis by road| despite some previous comments on Trip Advisor| though it was busy during the rush hour but this would apply to any hotel / resort in the Port Louis area unless you were staying at Caudan Waterfront.If you do come to Port Chambly and want to stock up the kitchen we'd recommend going a few miles to the South African supermarkets (Pick'n'Pay| Intermart & Food Lovers Paradise) at Grand Baie rather than the nearby Jumbo supermarket."])).todense()))
#
# print(nb.predict(tfidf_transformer.transform(vectorizer.transform(["Excellet place to stay withc decent rooms view and facilities.The rooms are neat and evrything just gr8.the only prob was the breakfast.. Not to great and very limited stuff. There are number of activities which one can enjoy boat ride| kayak| canoying etc.. the place is just beautiful.Not a beach hotel| but good location both for busniess and leisure.Its value for money."])).todense()))
# print(mn.predict(tfidf_transformer.transform(vectorizer.transform(["Excellet place to stay withc decent rooms view and facilities.The rooms are neat and evrything just gr8.the only prob was the breakfast.. Not to great and very limited stuff. There are number of activities which one can enjoy boat ride| kayak| canoying etc.. the place is just beautiful.Not a beach hotel| but good location both for busniess and leisure.Its value for money."])).todense()))
#
# print(nb.predict(tfidf_transformer.transform(vectorizer.transform(["Amazing location with a high sense of safety in the place. Nice view from the villa and very quiet place with nice live band music. We went down till the mouth of the river and it was very calm and peaceful. "])).todense()))
# print(mn.predict(tfidf_transformer.transform(vectorizer.transform(["Amazing location with a high sense of safety in the place. Nice view from the villa and very quiet place with nice live band music. We went down till the mouth of the river and it was very calm and peaceful. "])).todense()))
#
# print(nb.predict(tfidf_transformer.transform(vectorizer.transform(["run down| terrible customer service| cockroaches in restaurant| not enough cups| glasses etc at meal times| have stayed at 3* hotels which have been better then this. breakfast ample| other meal times poor. All inclusive absolute joke| cocktail was slush puppy machine 1 was non alcoholic & the other with alcohol| can honestly say 1 of the worst hotels have ever stayed in"])).todense()))
# print(mn.predict(tfidf_transformer.transform(vectorizer.transform(["run down| terrible customer service| cockroaches in restaurant| not enough cups| glasses etc at meal times| have stayed at 3* hotels which have been better then this. breakfast ample| other meal times poor. All inclusive absolute joke| cocktail was slush puppy machine 1 was non alcoholic & the other with alcohol| can honestly say 1 of the worst hotels have ever stayed in"])).todense()))

#print(mn.predict(tfidf_transformer.transform(vectorizer.transform([""])).todense()))
