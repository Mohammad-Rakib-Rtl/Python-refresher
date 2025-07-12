"""
For & While Loops
"""
my_list = [1, 2, 3, 4, 5]

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
#
# for x in my_list:
#     print(x)

# for x in range(3, 7):
#     print(x)

sum_of_for_loop = 0

for x in my_list:
    sum_of_for_loop += x

print(sum_of_for_loop)
print()

print("------String------")

string_list = ["ratul", "shunehara", "Nishita", "Harun"]

for x in string_list:
    print(f"Happy Holyday {x}!")
print()
print("------While------")

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")


























