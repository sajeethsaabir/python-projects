print("Please enter the amount of money you have")

usr_inp_1 = int(input("Dollars: "))
usr_inp_2 = int(input("Cents: "))

sum_1 = usr_inp_1 * 100 + usr_inp_2

sum_2 = sum_1 // 25

sum_3 = sum_1 % 25

sum_4 = sum_3 // 10

sum_5 = sum_3 % 10

sum_6 = sum_5 // 5

sum_7 = sum_5 % 5

coins = sum_2 + sum_4 + sum_6 + sum_7

print("Minumum Number of Coins = ", coins)
