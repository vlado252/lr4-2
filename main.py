# Запрашиваем у пользователя количество чисел, которые будут в списке
s = int(input("на сколько чисел нам нужен список:"))

# Создаем список, где каждый элемент - это квадрат числа, введенного пользователем
a = [int(input())**2 for i in range(1, s+1)]

# Выводим полученный список
print(a)
