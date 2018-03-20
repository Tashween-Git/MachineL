# import fileinput
#
filename = "E:\PycharmProjects\MachineL\Le Ravenal_test_duplicated.csv"
#
# seen = set() # set for fast O(1) amortized lookup
#
# for line in fileinput.FileInput(filename, inplace=1):
#     if line in seen: continue # skip duplicate
#
#     seen.add(line)
#     print(line) # standard output is now redirected to the file


inFile = open(filename,'r')
out = filename.replace("duplicated", "duplicated_cleaned")

outFile = open(out,'w', newline='')

listLines = []

for line in inFile:

    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()

inFile.close()