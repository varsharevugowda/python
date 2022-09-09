#Example 1: Read CSV
# import csv
# with open('C:\Users\varshitha.r\PycharmProjects\pythontask\department.csv') as csvfile:
#  data = csv.reader(csvfile, delimiter=' ')
#  for row in data:
#    print(' '.join(row))

#Example 2: Read CSV
# import csv
# with open('C:\\Users\\varshitha.r\\PycharmProjects\\pythontask\\department1.csv',) as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#
# #Example 3: Write to a CSV file
# import csv
# with open('C:\\Users\\varshitha.r\\PycharmProjects\\pythontask\\department1.csv', 'w') as file:
#     writer1 = csv.writer(file)
#     writer1.writerow(["SN", "Movie", "Protagonist"])
#     writer1.writerow([1, "Lord of the Rings", "Frodo Baggins"])
#     writer1.writerow([2, "Harry Potter", "Harry Potter"])
#
#Example 4: Writing multiple rows with writerows()
#If we need to write the contents of the 2-dimensional list to a CSV file, here's how we can do it.

# import csv
# csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
#                [2, "Harry Potter", "Harry Potter"],[3, "Hobbit", "Frodo Baggins"]]
# with open('C:\\Users\\varshitha.r\\PycharmProjects\\pythontask\\department1.csv', 'w',newline='') as file:
#     writer1 = csv.writer(file)
#     writer1.writerows(csv_rowlist)

# #Example 5: Python csv.DictReader()
# import csv
# with open("department1.csv", 'r') as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         print(dict(row))

#Example 6: Python csv.DictWriter()
# import csv
#
# with open('C:\\Users\\varshitha.r\\PycharmProjects\\pythontask\\department1.csv', 'w', newline='') as file: #CSV file where we want to write to
#     #fieldnames - a list object which should contain the column headers specifying the order in which data should be written in the CSV file
#     fieldnames = ['name', 'rating']
#     writer1 = csv.DictWriter(file, fieldnames=fieldnames)
#
#     writer1.writeheader() #fieldnames = ['name', 'rating']
#     writer1.writerow({'name': 'John', 'rating': 2870})
#     writer1.writerow({'name': 'Sam', 'rating': 2822})
#     writer1.writerow({'name': 'Peter', 'rating': 2801})
#     writer1.writerow({'name': 'varsha', 'rating': 2802})
#     writer1.writerow({'name': 'pallavi', 'rating': 2802})



#Example 7:Using the Pandas library to Handle CSV files
#Pandas is a popular data science library in Python for data manipulation and analysis.
# If we are working with huge chunks of data,
# it's better to use pandas to handle CSV files for ease and efficiency.

# import pandas as pd
# data=pd.read_csv("PandasCSV.csv")
# print(pd)
# print(data)

#exmaple8
#To write to a CSV file, we need to call the to_csv() function of a DataFrame.
import pandas as pd

# creating a data frame
df = pd.DataFrame([[0,'Jackv', 24], [1,'Rose2', 22]], columns = ['Sno','Name', 'Age'])

# writing data frame to a CSV file
df.to_csv('PandasCSV.csv')

#Example 9
# import pandas
# df = pandas.read_csv('PandasCSV.csv', index_col='Sno')
# print(df)

# import pandas
# df = pandas.read_csv('PandasCSV.csv', header=0,names=['Serial no', 'Employee name', 'Employee age'])
# print(df)

# #Inheritance in CSV
 import module
# import csv
#
# class Employee:
#
#     def employeeDetails(self):

#         with open('C:\\Users\\varshitha.r\\PycharmProjects\\pythontask\\department.csv', newline='') as csvfile:
#             data = csv.reader(csvfile, delimiter=' ', quotechar='|')
#             for row in data:
#                 print(', '.join(row))
#
#
# class Department(Employee):
#
#     def departmentDetails(self):
#         super()
#
#         with open('C:\\Users\\varshitha.r\\PycharmProjects\\pythontask\\department1.csv', newline='') as csvfile:
#             data = csv.reader(csvfile, delimiter=' ', quotechar='|')
#             for row in data:
#                 print(', '.join(row))
#
#
# # object of Manager class
# obj = Department()
#
# # output
# print("-----Employee Detail-----")
# print("name ,id ")
# obj.employeeDetails()
#
# print("-----Department Detail-----")
# obj.departmentDetails()
#
