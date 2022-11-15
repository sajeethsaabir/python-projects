print("Please enter the the number of coins you have")

user_input_1 = int(input("Quarter: "))
user_input_2 = int(input("Dime: "))
user_input_3 = int(input("Nicle: "))
user_input_4 = int(input("Penny: "))

quarter = 1 / 4
dime = 1 / 10
nicle = 1 / 20
penny = 1 / 100

monetary = user_input_1 * 25 + user_input_2 * \
    10 + user_input_3 * 5 + user_input_4 * 1

dollar = monetary // 100
cent = monetary % 100

print("The total is", dollar, "dollars and", cent, "cents")
