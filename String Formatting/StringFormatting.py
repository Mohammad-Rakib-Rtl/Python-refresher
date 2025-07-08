"""
String Formatting
"""

first_name = "RaT"
# print("Hi" + " " + first_name)
# print("Hi" + " " + first_name)
# print(f"Hi {first_name}" )


sentence = "Hi {} {}"
second_name = "Ratul"

print(sentence.format(first_name, second_name))
print(f"Hi! your first name is {first_name} and your second name is {second_name}.")
print(f"your love is {first_name}")
