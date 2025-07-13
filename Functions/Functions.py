"""
Functions
"""

# print("Hello and welcome to functions!")


def my_function():
    print("Inside my_function")

my_function()

def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

print_my_name("Mohammad", "Rakib")


def print_color_red():
    color = "Red" ###internal or local variable
    print(color)

color = "Blue" #### global variable
print(color)
print_color_red()


def print_numbers(highest_num, lowest_num):
    print(highest_num)
    print(lowest_num)

print_numbers(lowest_num=2, highest_num=10)



def multiply_numbers(a, b):
    return a * b

solution = multiply_numbers(19, 2)
print(solution)
# multiply_numbers(10, 2)

def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)

number_list = [2, 1, 7, 5, 6]
print_list(number_list)

print("------------------------------------")
print("Simple problem solve cost of item")
print("------------------------------------")

def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate

final_cost = buy_item(50)
print(final_cost)




























































































