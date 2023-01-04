def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as _error_:
        print(_error_)


def power(a, b):
    return a ** b


def remainder(a, b):
    return a % b


def history():
    if history_list:
        for index, calc in enumerate(history_list):
            print(calc)
    else:
        print("No calculations to show")
        return 0


def select_op(choice):
    if (choice == '?'):
        return history()
    if (choice == '#'):
        return -1
    elif (choice == '$'):
        return 0
    elif (choice in ('+', '-', '*', '/', '^', '%')):
        while (True):
            num_1_s = str(input("Enter first number: "))
            print(num_1_s)
            if num_1_s.endswith('$'):
                return 0
            if num_1_s.endswith('#'):
                return -1

            try:
                num_1_s = float(num_1_s)
                break
            except:
                print("Not a valid number,please enter again")
                continue

        while (True):
            num_2_s = str(input("Enter second number: "))
            print(num_2_s)
            if num_2_s.endswith('$'):
                return 0
            if num_2_s.endswith('#'):
                return -1
            try:
                num_2_s = float(num_2_s)
                break
            except:
                print("Not a valid number,please enter again")
                continue

        result = 0.0
        last_calculation = ""
        if choice == '+':
            result = add(num_1_s, num_2_s)
        elif choice == '-':
            result = subtract(num_1_s, num_2_s)
        elif choice == '*':
            result = multiply(num_1_s, num_2_s)
        elif choice == '/':
            result = divide(num_1_s, num_2_s)
        elif choice == '^':
            result = power(num_1_s, num_2_s)
        elif choice == '%':
            result = remainder(num_1_s, num_2_s)
        else:
            print("Something Went Wrong")

        final_calculation = "{0} {1} {2} = {3}".format(
            num_1_s, choice, num_2_s, result)
        print(final_calculation)
        history_list.append(final_calculation)
    else:
        print("Unrecognized operation")


while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")


choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
print(choice)
if (select_op(choice) == -1):
    # program ends here
    print("Done. Terminating")
    exit()
