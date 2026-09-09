import math
def priklad1(x, y, z):
    y1 = (x * x * x + y * y) / math.sqrt(z + 2)
    return y1

def priklad2(n):
    sum = 0
    kilkist = 0
    for i in range(1, 2*n, 2):
        sum += i
        kilkist += 1
    return sum, kilkist