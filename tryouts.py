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


# from sklearn import preprocessing
#
# le = preprocessing.LabelEncoder()
#
# le.fit(["Positive", "Negative"])
#
# print(le.classes_)
#
# print(le.transform(["Positive","Negative","Negative","Negative"]))


# train_dataset_array=['correct_equal_combined.csv','correct_equal_combined_pos_neg.csv','correct_equal_combined_pos_neg_no_3.csv']
# test_dataset_array=['test_correct_300_each.csv','test_correct_300_each_pos_neg.csv','test_correct_300_each_pos_neg_no_3.csv']
#
#
# train_dataset = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\' + train_dataset_array[0]
# test_dataset = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\' + test_dataset_array[0]
#
#
# print(train_dataset)
# print(test_dataset)

# import glob
# import os
#
# csv = []
# csv = (glob.glob("E:\PycharmProjects\TripAdvisorCrawl\*.csv"))
#
# for x in csv:
#     print(os.path.basename(x).replace(".csv", ""))

# import Naive
#
# Naive.predict("E:\PycharmProjects\MachineL\Hotels Dataset\\20 Degres Sud Hotel.csv")

# import csv
#
filename = "E:\PycharmProjects\MachineL\Hotels Dataset\Anahita Golf & Spa Resort.csv"
#
# with open(filename, 'r') as csvfile:
#     for row in csvfile:
#         print(row)
#         if(str(row) == "Comment Title, Comment"):
#             print("baba")



