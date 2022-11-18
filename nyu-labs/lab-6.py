print("Enter the prices of purchased items")
print("""Item_1:Higher price item
Item_2:Lower price item""")

item_1 = float(input("Item_1 Price: "))
item_2 = float(input("Item_2 Price: "))

dis_item_2 = item_2 / 2

price = item_1 + dis_item_2
print(price)

print("Enter 'y' if customer has club membership card otherwise enter 'n': ")
club_card = input("Is club card member? ")

if club_card == 'y':
    var_1 = price * 0.1
    price = price - var_1
    print(price)
else:
    print(price)

print("Enter the tax the tax rate")
tax = float(input("Tax: "))

tax_add = price * (tax / 100)
new_price = price + tax_add

print("The new price with discounts and tax added:", new_price)
