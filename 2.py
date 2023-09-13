# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def path_text(str_):
    *_, name_f = str_.split("/")
    str_ = str_.strip(name_f)
    n_f, expansion_f = name_f.split(".")
    return (str_, n_f, expansion_f)

str_ = "C:/Program Files/7-Zip/readme.txt"

print(*path_text(str_))
#print(type(path_text(str_)))

