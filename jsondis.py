#example 1
# from bs4 import BeautifulSoup
# #XML -eXTENSIBLE MARKUP LANGUAGE
# # Reading data from the xml file
# with open('Details.xml', 'r') as f:
#    data = f.read()
#    print(data)
#
# # Passing the data of the xml
# # file to the xml parser of
# # beautifulsoup
# bs_data = BeautifulSoup(data, 'xml')
#
# # A loop for replacing the value
# # of attribute `price` to WHAT !!
# # The tag is found by the clause
# # `bs_data.find_all('Product', {'name':'TV'})`
# for tag in bs_data.find_all('Product', {'name':'TV'}):tag["price"]="Hello!!!"

# Output the contents of the
# modified xml file
#print(bs_data.prettify())

# Example 2:
# Import the required modules
import xmltodict
import pprint

# Open the file and read the contents UNICODE TRANSFORMATION FORMAT
with open('Details.xml', 'r') as file:
   my_xml = file.read()

# Use xmltodict to parse and convert
# the XML document
my_dict = xmltodict.parse(my_xml) # xmltodict.parse to convert XML to PYTHONDICT

# Print the dictionary
pprint.pprint(my_dict, indent=4) # Reading complex data in a easier way(pretty print)
# # Example 3:
# # Program to convert an xml
# # file to json file
#
# # import json module and xmltodict
# # module provided by python
# import json
# import xmltodict
#
# # open the input xml file and read
# # data in form of python dictionary
# # using xmltodict module
# with open("Details.xml") as xml_file:
#     data_dict = xmltodict.parse(xml_file.read()) #XML TO DICT
#     #xml_file.close()
#
#     # generate the object using json.dumps()
#     # corresponding to json data
#
#     json_data = json.dumps(data_dict) #DICT TO JSON
#
#     # Write the json data to output
#     # json file
#     with open("data1.json", "w") as json_file: #JSON->DATA1.JSON
#         json_file.write(json_data)
#         #json_file.close()
