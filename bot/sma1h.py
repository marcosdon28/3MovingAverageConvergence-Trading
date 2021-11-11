import json

data = {}
for i in range(10):
    data[i] = i+1
    i = i+1

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
