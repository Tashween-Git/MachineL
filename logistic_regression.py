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

train_dataset_array=['correct_equal_combined.csv', 'correct_equal_combined_pos_neg.csv', 'correct_equal_combined_pos_neg_balanced.csv', 'correct_equal_combined_pos_neg_no_3.csv']
test_dataset_array=['test_correct_300_each.csv', 'test_correct_300_each_pos_neg.csv', 'test_correct_300_each_pos_neg.csv', 'test_correct_300_each_pos_neg_no_3.csv']


def predict(hotel_file):
    logistic(1)
    hotel_test = pd.read_csv(hotel_file, encoding='latin-1')

    X_test = hotel_test
    # print(X_test['Comment'].head())

    prediction_data = tdif.transform(count.transform(X_test['Comment'].values.astype('str')))

    predicted = mn.predict(prediction_data)
    total = 0
    # for x in predicted:
    #   print(x)

    return predicted

def predict_text(review):

    logistic(1)
    prediction_data = tdif.transform(count.transform([review])).todense()
    predicted = mn.predict(prediction_data)
    return predicted


def logistic(set):
    for i in range(set):

        #names =['CT','CS','C','D','M','R']

        train_dataset = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\' + train_dataset_array[i]
        test_dataset = 'E:\PycharmProjects\MachineL\Correct_observation_combined\\' + test_dataset_array[i]


        hotel = pd.read_csv(train_dataset, encoding='latin-1')
        hotel_test = pd.read_csv(test_dataset, encoding='latin-1')

        #print(hotel.head())

        #print(hotel.info())

        #print(hotel.describe())

        #print(hotel.columns)

        # print(hotel._ix[5,15,20])

        # print(hotel['Comments', 'Rating'])

        # print("Hello :")
        # print(hotel.groupby("Rating").Countries.describe())


        #for x in hotel:
        #    print(x)
        # Starting the process

        # X_train, X_test, y_train, y_test = train_test_split(hotel, hotel.Rating, test_size=0.5, shuffle=False)
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

        global count

        count = CountVectorizer()
        temp = count.fit_transform(X_train['Comment'].values.astype('str'))  # word count for recurrent words

        #print(count.get_feature_names())

        #print("temp: " + temp)

        global tdif

        tdif = TfidfTransformer()
        temp2 = tdif.fit_transform(temp) # Give words different Weights

        print(temp2.shape)

        #print(tdif)

        global mn

        mn = LogisticRegression()

        mn.fit(temp2, y_train)

        prediction_data = tdif.transform(count.transform(X_test['Comment'].values.astype('str')))

        predicted = mn.predict(prediction_data)

        # for c, d in zip(predicted, y_test):
        #     print(c, d)
        print(np.mean(predicted == y_test))

        print(accuracy_score(y_test,predicted))

        print("Printing how many was correct: ")
        print(accuracy_score(y_test,predicted, normalize=False))

        #print(list(predicted[:10]))

        #print(y_test[:10])

        #print(X_test.Comment[0])


        from sklearn.metrics import classification_report

        print("\n Classification report: \n")
        print(classification_report(y_test, predicted))

        from sklearn.metrics import confusion_matrix

        print("\n Confusion Matrix: \n")
        print(confusion_matrix(y_test, predicted))

        #print("\n\n\n Printing for custom sentence: ")
        #print(mn.predict(tdif.transform(count.transform(["The hotel was beautiful but the food was not good"]))))

#logistic(4)