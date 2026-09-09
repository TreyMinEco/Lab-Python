def piramida(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end = " ")
        print("")

n = int(input("Уведіть число N для побудови піраміди: "))
while n < 1 or n > 10:
    print("Помилка оберіть число N від 1 до 10")
    n = int(input("Уведіть число N для побудови піраміди: "))

piramida(n)
