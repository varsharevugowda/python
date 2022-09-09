import json

f=open("data.json","r")
details=json.load(f)

for i in details["employee"]:
    print(i)