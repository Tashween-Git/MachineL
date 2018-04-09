import Naive
import logistic_regression
import SVM

#n = Naive.naive(1)

clf_scrore = []
def get_average(hotel_name):

    #predicted = Naive.predict("E:\PycharmProjects\MachineL\Correct_observation_combined\Le Meridien Ile Maurice.csv")

    X= [Naive, SVM, logistic_regression]

    for clf in X:
        predicted = clf.predict(hotel_name)

        #print(predicted.shape)
        #print(predicted.shape[0])

        total = 0
        for x in predicted:
            total = total + x
            #print(x)

        average = total/predicted.shape[0]

        average = float(average)
        average = ("%.1f" % average)

        clf_scrore.append(average)

    return clf_scrore
        #print(average)