# 2. Write a Python program to convert Python object to JSON data.

import json
# a Python object (dict):
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}

print(type(python_obj))
# convert into JSON: 
# dump() dump data to file, file argument is neccesary
# dumps() dump data as a string
json_obj = json.dumps(python_obj)


print(type(json_obj))
# result is a JSON string:
print(json_obj)
