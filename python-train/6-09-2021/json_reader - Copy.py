import json 
escaper ={ 
  "New line": "Hello\nWorld", 
  "Horizontal tab": "Hello\tWorld", 
  "Double quote": "Hello \"World\""
} 
# Serializing json  
json_object = json.dumps(escaper, indent = 4) 
print(json_object)
data = escaper

print('*******************') 
for i in data:
	print(i)
print('*******************')

for i in data:
	print(data[i])