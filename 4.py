# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def fibbonachi(n):
    num1 = 1
    num2 = 1
    for i in range(2, n):
        num1, num2 = num2, num1 + num2
        yield num2


number = int(input("Введите число: "))
print(1, 1, end=" ")
for i, num in enumerate(fibbonachi(number)):
    print(num, end=" ")
