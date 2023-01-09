def count_sheep(n):
    sheep_count = ""

    for count in range(1, n+1):
        sheep_count += str(count) + "sheep... "
    return sheep_count
