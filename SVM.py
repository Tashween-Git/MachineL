#Loading dataset from a csv format using Pandas
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn import svm

from sklearn.feature_extraction.text import TfidfTransformer

from sklearn import metrics
# For preprocessing the data
from sklearn.preprocessing import Imputer
from sklearn import preprocessing

# To calculate the accuracy score of the model
from sklearn.metrics import accuracy_score

filename = 'Trou aux Biches Beachcomber Golf Resort & Spa.csv'
filename1 = 'Clean_1.csv'

train_dataset_array=['correct_equal_combined.csv', 'correct_equal_combined_pos_neg.csv', 'correct_equal_combined_pos_neg_balanced.csv', 'correct_equal_combined_pos_neg_no_3.csv']
test_dataset_array=['test_correct_300_each.csv', 'test_correct_300_each_pos_neg.csv', 'test_correct_300_each_pos_neg.csv', 'test_correct_300_each_pos_neg_no_3.csv']

for i in range(4):

    train_dataset = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\' + train_dataset_array[i]
    test_dataset = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\' + test_dataset_array[i]


    #names =['CT','CS','C','D','M','R']

    # hotel = pd.read_csv(filename1)

    hotel = pd.read_csv(train_dataset, encoding='latin-1')
    hotel_test = pd.read_csv(test_dataset, encoding='latin-1')

    # print("head(): \n")
    # print(hotel.head())
    #
    # print("info(): \n")
    #
    # print(hotel.info())
    #
    # print("describe(): \n")
    #
    # print(hotel.describe())
    #
    # print("columns(): \n")
    #
    # print(hotel.columns)
    #
    # # print(hotel._ix[5,15,20])
    #
    # # print(hotel['Comments', 'Rating'])
    #
    # print("1. Handling missing data(): \n")
    # print("Checking null(): \n")
    # print(hotel.isnull().sum())  # Handling missing data
    #
    # print("checking for '?' presence: \n")
    # # for value in hotel.columns:
    # #     print(value, ":", sum(hotel[value] == '?'))
    #
    # hotel_dup = hotel  # duplicating before pre processing
    #
    # # Performing Imputation
    # print("2. Performing Imputation: \n")
    #
    # # summary of all attributes in the dataset
    # print("hotel_dup summary for all attributes(): \n")
    # print(hotel_dup.describe(include='all'))

    X_train = hotel
    y_train = hotel.Rating
    if i>0:
        y_train = hotel.Polarity

    X_test = hotel_test
    y_test = hotel_test.Rating
    if i>0:
        y_test = hotel_test.Polarity

    print(hotel.shape)
    print(X_train.shape)
    print(y_train.shape)


    count = CountVectorizer()

    temp = count.fit_transform(X_train['Comment'].values.astype('str'))  # word count for recurrent words

    # print("Features:")
    #
    # print(count.get_feature_names())
    # print(len(count.get_feature_names()))

    #print("Stop Words:")
    #print(count.get_stop_words())
    #print(len(count.get_stop_words()))


    print(temp.shape)

    #print("temp: " + temp)

    tdif = TfidfTransformer()
    temp2 = tdif.fit_transform(temp)  # Give words different Weights


    print(temp2.shape)

    #svm_clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape='ovr',
    #                  degree=3, gamma='auto', kernel='rbf', max_iter=-1, probability=False, random_state=None,
    #                  shrinking=True, tol=0.001, verbose=False)

    svm_clf = svm.LinearSVC(C=0.5, class_weight=None, dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,
     verbose=0)

    svm_clf.fit(temp2, y_train)


    prediction_data = tdif.transform(count.transform(X_test['Comment'].values.astype('str')))

    predicted = svm_clf.predict(prediction_data)

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


    print(np.mean(predicted == y_test))
    print(metrics.accuracy_score(y_test, predicted))

    from sklearn.metrics import classification_report

    print("\n Classification report: \n")
    print(classification_report(y_test, predicted))

    from sklearn.metrics import confusion_matrix

    print("\n Confusion Matrix: \n")
    print(confusion_matrix(y_test, predicted))

    print("Starting for custom")
    print(svm_clf.predict(tdif.transform(count.transform(["Hilton Mauritius is a very good resort all together especially their facilities but some of the staff aren't the best and some times aren't very hospitable. The hotel also has hidden costs for dinner at their beach restaurant and doesn't say about the supplement charge."])).todense()))

                # Start of new Vectorizer
                #########################
    def bigram_vectorizer():
        bigram = CountVectorizer(stop_words='english', token_pattern=r'\b\w+\b', ngram_range=(1, 2), min_df=0.0039, max_df=0.8)
        temp_bigram = bigram.fit_transform(X_train['Comment'].values.astype('str'))  # word count for recurrent words

        tdif_bigram = TfidfTransformer(norm='l1', smooth_idf=False)
        temp2_bigram = tdif_bigram.fit_transform(temp_bigram)  # Give words different Weights

        svm_clf.fit(temp2_bigram, y_train)
        prediction_data_bigram = tdif_bigram.transform(bigram.transform(X_test['Comment'].values.astype('str')))

        predicted_bigram = svm_clf.predict(prediction_data_bigram)

        print(np.mean(predicted_bigram == y_test))
        print(metrics.accuracy_score(y_test, predicted_bigram))


    def custom_tokenizer():
        from nltk import word_tokenize
        from nltk.stem import WordNetLemmatizer
        import nltk
        #nltk.download('wordnet')

        class LemmaTokenizer(object):
            def __init__(self):
                self.wnl = WordNetLemmatizer()

            def __call__(self, doc):
                return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]

        vect = CountVectorizer(tokenizer=LemmaTokenizer(), ngram_range=(1, 2), stop_words='english', min_df=10, max_df=0.8)
        temp_bigram = vect.fit_transform(X_train['Comment'].values.astype('str'))  # word count for recurrent words

        print(temp.shape)
        tdif_bigram = TfidfTransformer(norm='l1', smooth_idf=False)
        temp2_bigram = tdif_bigram.fit_transform(temp_bigram)  # Give words different Weights

        svm_clf.fit(temp2_bigram, y_train)
        prediction_data_bigram = tdif_bigram.transform(vect.transform(X_test['Comment'].values.astype('str')))

        predicted_bigram = svm_clf.predict(prediction_data_bigram)

        print(np.mean(predicted_bigram == y_test))
        print(metrics.accuracy_score(y_test, predicted_bigram))

        from sklearn.metrics import confusion_matrix
        print("\n Confusion Matrix: \n")
        print(confusion_matrix(y_test, predicted))

    #bigram_vectorizer()
    #custom_tokenizer()


# print(nb.predict(tfidf_transformer.transform(vectorizer.transform(["Very disappointing and bad, didn't expect such crap service"])).todense()))
# print(mn.predict(tfidf_transformer.transform(vectorizer.transform(["Very disappointing and bad, didn't expect such crap service"])).todense()))
#Hilton Mauritius is a very good resort all together especially their facilities but some of the staff aren't the best and some times aren't very hospitable. The hotel also has hidden costs for dinner at their beach restaurant and doesn't say about the supplement charge.

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
