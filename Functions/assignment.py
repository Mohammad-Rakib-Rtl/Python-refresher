"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""

def my_function(firstname, lastname, age):
    my_dictionary = {
        "First name": firstname,
        "Last name": lastname,
        "Age": age
    }

    return my_dictionary

print_dict = my_function(lastname="Ratul",firstname="MD",age=27)
print(print_dict)


































































































