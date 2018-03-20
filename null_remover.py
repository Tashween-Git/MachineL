import csv
import pandas as pd

filename = "E:\PycharmProjects\MachineL\Le Ravenal_test.csv"

hotel = pd.read_csv(filename, encoding='latin-1')

print(hotel.info())

input = open(filename, 'r')
out = filename.replace("test", "test_cleaned")
output = open(out, 'w', newline='')
writer = csv.writer(output)
for row in csv.reader(input):
    # if row:
    #     writer.writerow(row)
    if any(field.strip() for field in row):
        writer.writerow(row)
input.close()
output.close()
