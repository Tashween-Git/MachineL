import Naive

#n = Naive.naive(1)

def get_average(hotel_name):

    #predicted = Naive.predict("E:\PycharmProjects\MachineL\Correct_observation_combined\Le Meridien Ile Maurice.csv")
    predicted = Naive.predict(hotel_name)

    #print(predicted.shape)
    #print(predicted.shape[0])

    total = 0
    for x in predicted:
        total = total + x
        #print(x)

    average = total/predicted.shape[0]

    return average
    #print(average)