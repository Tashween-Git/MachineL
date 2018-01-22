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

pos =0

pos = pos +1
print(pos)