from mod import priklad1
from mod import priklad2

print("Виберіть з чим працювати:")
print("Введіть 1 - якщо хочете вирішити приклад: (x * x * x + y * y) / math.sqrt(z + 2)")
print("Введіть 2 - якщо хочете вивести суму і кількість елементів ряду y=1*3*5*...*(2*n-1)")

number = int(input("Ведіть номер 1 або 2: "))

if number == 1:
    print("Працюємо із виразок (x * x * x + y * y) / math.sqrt(z + 2)")
    x = int(input("Введіть x: "))
    y = int(input("Введіть y: "))
    z = int(input("Введіть z: "))
    result1 = priklad1(x, y, z)
    print("Результат до обрахунку вираза (x * x * x + y * y) / math.sqrt(z + 2) =", result1)

elif number == 2:
    print("Працюємо із виводом суми і кількості елементів ряду y=1*3*5*...*(2*n-1)")
    sum, kilkist = priklad2(20)
    print("Сума ряду y=1*3*5*...*(2*n-1) =", sum)
    print("Кількість елементів ряду:", kilkist)

else:
    print("Помилка треба було ввести число від 1 до 2!")
