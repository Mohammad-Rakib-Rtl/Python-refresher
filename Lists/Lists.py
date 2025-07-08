"""

Lists are a collection of data
"""

my_list = [20, 12, 27, 16, 13]
print(my_list)
print(f"index num 1st is: {my_list[0]}")

people_list = ["Ratul", "Karim", "Rafiq"]
print(people_list)
print(f"second people is in this index: {people_list[-2]}")
print(len(people_list))

#### Slicing
print(people_list[0:2])

### append
my_list.append(12)
print(my_list)

### insert
my_list.insert(1, 200)
print(my_list)

### remove
my_list.remove(12)
print(my_list)

# my_list.remove(12)
# print(my_list)
#
# my_list.remove(12)
# print(my_list)

### pop()

my_list.pop(1)
print(my_list)


### sort

my_list.sort()
print(my_list)

























