import csv
with open('C:\pandascsvfiles\image.csv',newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ',quotechar='|')
 for row in data:
   print(' '.join(row))
#--------------------------------------------------
import csv
with open('image1.csv', 'w', newline='') as file:
    writer1 = csv.writer(file)
    writer1.writerow(["file_name", "file_size", "img_res","img_name","no_of_obj","obj_res"])
    writer1.writerow(["flower", "400mb", "100px","rose","12","300px"])
    writer1.writerow(["laptop", "600mb", "170px","dell","6","350px"])
# --------------------------------------------------------------------------------
# import csv
# class Base:
#     def openfile(self):
#         with open('C:\\Users\\varshitha.r\\PycharmProjects\\pythontask',newline='') as csvfile:
#             data = csv.reader(csvfile, delimiter='\t', quotechar='|')
#             for row in data:
#                 print(','.join(row))
# class Derived(Base):
#     def read(self):
#         super()
#         with open('image.csv','r', newline='') as csvfile:
#             data = csv.reader(csvfile, delimiter='\t', quotechar='|')
#             for row in data:
#                 print(','.join(row))
# d=Derived()
# d.openfile()
#d.read()
# d.write()