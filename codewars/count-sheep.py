def count_sheep(n):
    sheep_count = ""

    for count in range(1, n+1):
        sheep_count += str(count) + "sheep... "
    return sheep_count


testVar1 = print(count_sheep(4))
testVar1 = print(count_sheep(6))
