import requests, json

# Google for JSON fro covid19 india
r = requests.get("https://api.covid19india.org/state_district_wise.json")
data = r.json()

with open('covid19Data.json','w') as outfile:
	json.dump(data, outfile, indent=2)  # since we are dumping to file use dump() not dumps()




