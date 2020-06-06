import json

covidDic = {}

with open('covid19Data.json') as json_file:
    data = json.load(json_file)
    covidDic = data   
    # print(data)

# Get data of particular city
gzb_data = covidDic['Uttar Pradesh']['districtData']['Ghaziabad']
# print(gzb_data)

# Output we got
# {'notes': '', 'active': 87, 'confirmed': 172, 'deceased': 2, 'recovered': 83, 'delta': {'confirmed': 0, 'deceased': 0, 'recovered': 0}}
# here we are intereseted in only four keys
# 'active': 87, 'confirmed': 172, 'deceased': 2, 'recovered': 83
# we can del remaining keys
del gzb_data['notes']
del gzb_data['delta']

# print(gzb_data)
# print(type(gzb_data))
print('Ghaziabad Covid 19 Status Update')
print('********************************')
for key, value in gzb_data.items():
	print(f'{key.title()} : {value}')

print() # for extra space

udp_data = covidDic['Rajasthan']['districtData']['Udaipur']

del udp_data['notes']
del udp_data['delta']

print('Udaipur Covid 19 Status')
print('**************************')
for key,value in udp_data.items():
	print(f'{key.title()} : {value}')