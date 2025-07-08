"""
String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.
"""

left_days = input("How many days until your birthday left? please enter integer number:  ")

apprx_week = (int(left_days) / 7 )

print(f"You have approximately {round(apprx_week, 2)} week left. Thank you :)")