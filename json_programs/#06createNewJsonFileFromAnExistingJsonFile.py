# 6. Write a Python program to create a new JSON file from an existing JSON file.

import json

with open('IndianStates.json','r') as json_file:
  state_data= json.load(json_file)

with open('new_states.json', 'w') as json_file:
  json.dump(state_data, json_file, indent=2)
