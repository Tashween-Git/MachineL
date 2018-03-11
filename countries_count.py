#Loading dataset from a csv format using Pandas
import numpy as np
import pandas as pd
import collections

filename = 'E:\PycharmProjects\MachineL\Countries\country.csv'

countries_ds = pd.read_csv(filename, encoding="latin-1")

countries = countries_ds.Countries


hotel = pd.read_csv('E:\PycharmProjects\MachineL\\Null_removed.csv', encoding="latin-1")

hotel_countries = hotel.Countries

mru = collections.Counter()

count =0
country_count= [[]]

f = open("population_count.csv", "w")

f.write("Country, Count \n")

for country in countries:
    for hotel in hotel_countries:
        #print(hotel)
        if str(country).lower() in str(hotel).lower():
            count = count + 1

    f.write(country + "," + str(count) + "\n")

    print(country + ":" + str(count))
    count = 0

f.close()