# 1. Write a Python program to convert JSON data to Python object.

import json

# Json data
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'

# By using json.loads we can convert Json object to python object
python_obj = json.loads(json_obj)

print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"]) 
