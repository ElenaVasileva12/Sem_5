# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя».


def simple_num(n):
    list_1 = []
    v = []
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            if i % j == 0:
                list_1.append(i)
    for i in list_1:
        if list_1.count(i) == 1:
            v.append(i)
    yield v


n = int(input("Введите простое число: "))

print(*simple_num(n))
