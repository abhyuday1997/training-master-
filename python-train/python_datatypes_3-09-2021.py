# Lists
students = ['Abhyuday', 'aaron', 'cody']

for x in students:
    print('Hi,' + x.title() + "!")

dogs = ['border collie', 
        'australian cattle dog', 
        'labrador retriever']
print("Printing every_element and changing to dogs")
for x in dogs:
	print(x.title())

print('Accessing_last_element_of list_named_dogs')
print(dogs[-1].title())

print("Appending sentence to dogs")

for x in dogs:
	print('I like' + x + 's.')
	
print ("Enumerating to keep track of index of current item in list")

for i,j in enumerate(dogs):
	print("index: " + (str(i)) + j.title())

print("Modifying elements in list")

dogs_n = ['border collie', 'australian cattle dog', 'labrador retriever']

dogs_n[0] = 'australian shepherd'
print(dogs_n)

print("finding index of particular element like 'labrador retriever' and 'poodle' ")
print(dogs_n.index('australian cattle dog'))
for x in dogs_n:
	print(x)

print('checking whether element exist is list')
boolian = 'poodle' in dogs_n
print('Poodle is in dogs list: {}',boolian)