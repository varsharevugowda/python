import csv
with open("C:\\Users\\varshitha.r\\PycharmProjects\\pythontask\\department.csv") as csvfile:
 data = csv.reader(csvfile, delimiter=' ')
 for row in data:
   print(' '.join(row))