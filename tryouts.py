# import pandas as pd
#
#
# filename1 = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\correct_equal_combined.csv'
#
# hotel = pd.read_csv(filename1, encoding='latin-1')
#
#
# print(hotel.head())
#
# hotel = hotel.drop(['Mobile','Countries', 'Date'], axis=1)
#
# print(hotel.head())
#
# print(hotel.dtypes)
#
# # Checking for any null attributes
# print(hotel[hotel.isnull().any(axis=1)])
#
# # # checking highest common value first
# # hotel["xxx"].value_counts()
# #
# # #Replacing null with highest common
# # hotel = hotel.fillna({"xxx": "xxhighestxx"})
#

# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.linear_model import LogisticRegression
#
# from sklearn.naive_bayes import GaussianNB, MultinomialNB
#
# from sklearn.feature_extraction.text import TfidfTransformer
#
#
# count = CountVectorizer(stop_words=None, tokenizer=None, ngram_range=(1, 1))
# temp = count.fit_transform(["Very disappointing and bad, didn't expect such  crap crap crap service", "The hotel was beautiful but the food was very bad"])  # word count for recurrent words
#
#
# print(count.get_feature_names())
#
# print("Stop Words:")
# print(count.get_stop_words())
# print(temp.shape)
#
# tdif = TfidfTransformer(norm='l1')
# temp2 = tdif.fit_transform(temp) # Give words different Weights
#
# print(temp2)


from sklearn import preprocessing

le = preprocessing.LabelEncoder()

le.fit(["Positive", "Negative"])

print(le.classes_)

print(le.transform(["Positive","Negative","Negative","Negative"]))
