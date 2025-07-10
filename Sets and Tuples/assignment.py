'''
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals

'''


animals = ["cat", "dog", "cow", "chicken", "duck" ]

animals.pop(2)
print(animals)

animals.append("Black wolf")
print(animals)

animals.remove("cat")
print(animals)
for x in animals:
    print(x)

print(animals[:])
print(animals[0:3])