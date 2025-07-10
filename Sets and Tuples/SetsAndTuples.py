"""
Sets are similar to lists but are unordered and cannot contain duplications
use curly brackets
"""

'''
Sets are typically used when we want really fast organization or we want 
to remove duplications from a list.

'''


print("--------------------------")
print("SET")
print("--------------------------")

my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)
print(len(my_set))

for x in my_set:
    print(x)

### REMOVE element from set

my_set.discard(5)
print(my_set)

# my_set.clear()
# print(my_set)

my_set.add(6)
print(my_set)

## if we want to add more than 1 then use UPDATE

my_set.update([7, 8, 9])
print(my_set)

'''

Tuples are used often when you don't want to data to 
be changed within a list as they are an unchageable.

'''

print("--------------------------")
print("TUPLE")
print("--------------------------")

my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))
print(my_tuple[3])

my_tuple[2] = 2
print(my_tuple)



'''
Lists are definately the most used out
of the three most common data structures.
'''
















