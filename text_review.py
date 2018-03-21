import Naive

#n = Naive.naive(1)

def get_rating(review):

    #predicted = Naive.predict("E:\PycharmProjects\MachineL\Correct_observation_combined\Le Meridien Ile Maurice.csv")
    rating = Naive.predict_text(review)

    return rating
    #print(average)