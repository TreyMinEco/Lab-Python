def znach_a_b():
    a = int(input("Введіть А: "))
    while a < 1 or a > 100:
        print("Помилка значення А має бути від 1 до 100")
        a = int(input("Введіть А: "))

    b = int(input("Введіть В: "))
    while b < 1 or b > 100:
        print("Помилка значення В має бути від 1 до 100")
        b = int(input("Введіть В: "))
    return a, b

def calculate(a, b):
    if a > b:
        x = a / b + 1
    elif a == b:
        x = a + 25
    else:
        x = (a * b - 2) / a

    return x

a, b = znach_a_b()
x = calculate(a, b)
print("X=", x)
