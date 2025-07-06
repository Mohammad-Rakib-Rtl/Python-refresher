"""
Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.
"""
wallet_hav = 50
item_price = 15
total_tax = (item_price + ((item_price * 3) / 100))
money_left = wallet_hav - total_tax

print(money_left)