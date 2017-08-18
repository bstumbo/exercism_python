def square_of_sum(num):
    return sum(x for x in range(1, num + 1))**2 - sum(y**2 for y in range(1, num + 1))
