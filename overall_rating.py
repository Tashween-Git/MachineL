import Naive

n = Naive.naive(1)

predicted = Naive.predict("E:\PycharmProjects\MachineL\Correct_observation_combined\Le Meridien Ile Maurice.csv")

print(predicted.shape)
print(predicted.shape[0])

total = 0
for x in predicted:
    total = total + x
    #print(x)

average = total/predicted.shape[0]

print(average)