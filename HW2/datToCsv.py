import csv

# read flash.dat to a list of lists
datContent = [i.strip().split() for i in open("T10I4D100K.dat").readlines()]

print(datContent)

# write it as a new CSV file
with open("./flash.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)