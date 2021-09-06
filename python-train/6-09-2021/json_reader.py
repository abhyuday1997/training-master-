import json
f = open (r'escape_sequence.json', "r")
# Reading from file
data = json.loads(f.read())

print('*******************') 
for i in data:
	print(i)
print('*******************')

for i in data:
	print(data[i])
#print(data['secretBase'])
