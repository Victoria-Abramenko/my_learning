# # ___________________ задача №1 ___________________
# print("Привет, Яндекс!") #Привет, Яндекс!

# # ___________________ задача №2 ___________________
# name = input("Как Вас зовут?")#Вика
# print(f"Привет, {name}")#Привет, Вика

# # ___________________ задача №3 ___________________
# stroke = input()#2 + 2 = 4
# print(stroke)#2 + 2 = 4
# print(stroke)#2 + 2 = 4
# print(stroke)#2 + 2 = 4

# # ___________________ задача №4 ___________________
# money = int(input())#100
# price = int(2.5 * 38)
# get = money - price
# print(get)#5

# # ___________________ задача №5 ___________________
# num_1 = int(input())#2
# num_2 = int(input())#3
# num_3 = int(input())#10
# print(num_3 - (num_1 * num_2))#4

# # ___________________ задача №6 ___________________
# name = input()#черешня
# price = int(input())#2
# weight = int(input())#3
# money = int(input())#10
# sum_num = price * weight
# get_money = money - sum_num
# print("Чек")#Чек
# print(f"{name} - {weight}кг - {price}руб/кг")# черешня - 3кг - 2руб/кг
# print(f"Итого: {sum_num}руб")# Итого: 6руб
# print(f"Внесено: {money}руб")# Внесено: 10руб
# print(f"Сдача: {get_money}руб")# Сдача: 4руб

# # ___________________ задача №7 ___________________
# num = int(input())#3
# phrase = "Купи слона!\n"
# print(phrase * num)
# #Купи слона!
# #Купи слона!
# #Купи слона!

# # ___________________ задача №8 ___________________
# num = int(input())#3
# phrase = input()#Попка дурак!
# phrase_2 = "Я больше никогда не буду писать "
# phrase_3 = f'{phrase_2}"{phrase}"!\n'
# print(phrase_3 * num)
# # Я больше никогда не буду писать "Попка дурак!"!
# # Я больше никогда не буду писать "Попка дурак!"!
# # Я больше никогда не буду писать "Попка дурак!"!

# # ___________________ задача №9 ___________________
# num_1 = int(input())#10
# num_2 = int(input())#10
# print(int(num_1 * num_2 / 2))#50

# # ___________________ задача №10 ___________________
# name = input()#Ванечка
# num = int(input())#832
# num_2 = num // 100
# num_3 = num % 100 // 10
# num_4 = num % 10
# print(f"Группа №{num_2}.")
# print(f"{num_4}. {name}.")
# print(f"Шкафчик: {num}.")
# print(f"Кроватка: {num_3}.")
# #Группа №8.
# #2. Ванечка.
# #Шкафчик: 832.
# #Кроватка: 3.

# # ___________________ задача №11 ___________________
# num = int(input())#1234
# a = num // 1000
# b = num // 100 % 10
# c = num // 10 % 10
# d = num % 10
# print(int(f"{b}{a}{d}{c}"))#2143

# # ___________________ задача №12 ___________________
# num_1 = int(input())#123
# num_2 = int(input())#99
# c = (num_1 % 10 + num_2) % 10
# b = ((num_1 // 10 % 10) * 10 + num_2) // 10 % 10
# a = ((num_1 // 100) * 100 + num_2) % 1000 // 100
# print(int(f"{a}{b}{c}"))#112

# # ___________________ задача №13 ___________________
# children = int(input())#3
# candy = int(input())#100
# num_1 = candy // children
# num_2 = candy % children
# print(num_1)#33
# print(num_2)#1

# # ___________________ задача №14 ___________________
# red = int(input())#1
# green = int(input())#2
# blue = int(input())#3
# num = red + blue + 1
# print(num)#5

# # ___________________ задача №15 ___________________
# hour = int(input())#8
# minutе = int(input())#0
# minutе_1 = int(input())#65
# total_minutes = hour * 60 + minutе
# delivery = total_minutes + minutе_1
# hour_2 = delivery // 60 % 24
# minute_2 = delivery % 60 % 60
# print(f"{hour_2:0>2}:{minute_2:0>2}")#09:05

# # ___________________ задача №16 ___________________
# a = int(input())#10
# b = int(input())#32
# c = int(input())#5
# lenght = b - a
# t = lenght / c
# print(f"{t:.2f}")#4.40

# # ___________________ задача №17 ___________________
# num_10 = input()#123
# num_2 = input()#1101
# print(int(num_10, 10) + int(num_2, 2))#136

# # ___________________ задача №18 ___________________
# price = input()#1001001
# money = input()#100
# print(int(money) - int(price, 2))#27

# # ___________________ задача №19 ___________________
# name = input()#манго
# price = int(input())#187
# weight = int(input())#43
# money = int(input())#8041
# w_p = f"{weight}кг * {price}руб/кг"
# total = price * weight
# m_p = money - total
# print("================Чек================")
# print(f"Товар:{name: >29}")
# print(f"Цена:{w_p: >30}")
# print(f"Итого:{total: >26}руб")
# print(f"Внесено:{money: >24}руб")
# print(f"Сдача:{m_p: >26}руб")
# print("===================================")
# #================Чек================
# #Товар:                        манго
# #Цена:              43кг * 187руб/кг
# #Итого:                      8041руб
# #Внесено:                    8041руб
# #Сдача:                         0руб
# #===================================

# # ___________________ задача №20 ___________________
# n = int(input())#32
# m = int(input())#285
# k_1 = int(input())#300
# k_2 = int(input())#240
# n_1 = int((m - k_2) * n / (k_1 - k_2))
# n_2 = int(n - n_1)
# print(n_1, n_2)#24 8

# # ___________________ задача №21 ___________________
# print("Как Вас зовут?")
# name = input()#Аня
# print(f"Здравствуйте, {name}!")
# print("Как дела?")
# queshion = input()#хорошо
# if queshion == "хорошо":
#     print("Я за вас рада!")
# elif queshion == "плохо":
#     print("Всё наладится!")
# #Я за вас рада!

# # ___________________ задача №22 ___________________
# speed_p = int(input())#10
# speed_v = int(input())#5
# if speed_p > speed_v:
#     print("Петя")
# elif speed_p < speed_v:
#     print("Вася")
# #Петя

# # ___________________ задача №23 ___________________
# speed_p = int(input())#10
# speed_v = int(input())#5
# speed_t = int(input())#7
# if speed_p > speed_v and speed_p > speed_t:
#     print("Петя")
# elif speed_v > speed_p and speed_v > speed_t:
#     print("Вася")
# elif speed_t > speed_p and speed_t > speed_v:
#     print("Толя")
# #Петя

# # ___________________ задача №24 ___________________
# speed_p = int(input())#5
# speed_v = int(input())#7
# speed_t = int(input())#10
# if speed_p > speed_v > speed_t:
#     print("1. Петя")
#     print("2. Вася")
#     print("3. Толя")
# elif speed_p > speed_t > speed_v:
#     print("1. Петя")
#     print("2. Толя")
#     print("3. Вася")
# elif speed_v > speed_t > speed_p:
#     print("1. Вася")
#     print("2. Толя")
#     print("3. Петя")
# elif speed_v > speed_p > speed_t:
#     print("1. Вася")
#     print("2. Петя")
#     print("3. Толя")
# elif speed_t > speed_p > speed_v:
#     print("1. Толя")
#     print("2. Петя")
#     print("3. Вася")
# elif speed_t > speed_v > speed_p:
#     print("1. Толя")
#     print("2. Вася")
#     print("3. Петя")
# #1. Толя
# #2. Вася
# #3. Петя

# # ___________________ задача №25 ___________________
# n = int(input())#3
# m = int(input())#5
# num_p = 7 - 3 + 2 + n
# num_v = 6 + 3 + 5 - 2 + m
# if num_p > num_v:
#     print("Петя")
# elif num_p < num_v:
#     print("Вася")
# #Вася

# # ___________________ задача №26 ___________________
# year = int(input())#2022
# num = year % 4
# if num == 0:
#     print("YES")
# else:
#     print("NO")
# #NO

# # ___________________ задача №27 ___________________
# num = int(input())#2332
# d = int(num % 10)
# c = int(num % 100 / 10)
# b = int(num % 1000 / 100)
# a = int(num / 1000)
# if a == d and b == c:
#     print("YES")
# else:
#     print("NO")
# #YES

# # ___________________ задача №28 ___________________
# phrase = input()#березка елочка зайка волк березка
# if "зайка" in phrase:
#     print("YES")
# else:
#     print("NO")
# #YES

# # ___________________ задача №29 ___________________
# name_1 = input()#Вова
# name_2 = input()#Аня
# name_3 = input()#Боря
# if name_1 < name_2 and name_1 < name_3:
#     print(name_1)
# elif name_2 < name_1 and name_2 < name_3:
#     print(name_2)
# elif name_3 < name_1 and name_3 < name_1:
#     print(name_3)
# #Аня

# # ___________________ задача №30 ___________________
# num = int(input())#123
# a = int(num / 100)
# b = int(num % 100 / 10)
# c = int(num % 10)
# num_1 = a + b
# num_2 = b + c
# if num_1 > num_2:
#     print(f"{num_1}{num_2}")
# else:
#     print(f"{num_2}{num_1}")
# #53

# # ___________________ задача №31 ___________________
# num = int(input())#123
# a = int(num / 100)
# b = int(num % 100 / 10)
# c = int(num % 10)
# num_min = min(a, b, c)
# num_max = max(a, b, c)
# if a != num_min and a != num_max:
#     num_3 = a
# elif b != num_min and b != num_max:
#     num_3 = b
# elif c != num_min and c != num_max:
#     num_3 = c
# else:
#     num_3 = 0
# if num_min + num_max == num_3 * 2:
#     print("YES")
# else:
#     print("NO")
# #YES

# # ___________________ задача №32 ___________________
# a = int(input("Введите число a: "))#10
# b = int(input("Введите число b: "))#15
# c = int(input("Введите число c: "))#12
# if a > b:
#     if a > c:
#         print("Максимальное из этих трех чисел число a")
#     else:
#         print("Максимальное из этих трех чисел число c")
# else:
#     if b > c:
#         print("Максимальное из этих трех чисел число b")
#     else:
#         print("Максимальное из этих трех чисел число c")
# # Максимальное из этих трех чисел число b

# # ___________________ задача №33 ___________________
# n = int(input("Введите натуральное число: "))#6
#
# p = 1
#
# for i in range(1, n + 1):
#     p *= i
#
# print(f"Факториал числа {n} = {p}")#720

# # ___________________ задача №34 ___________________

# for i in range(1 , 7):
#     print("*" * i)
# # *
# # **
# # ***
# # ****
# # *****
# # ******

# # ___________________ задача №35 ___________________
# # Что выведет код?
# a = {1: "A", 2: "B", 3: "C"}
# b = a.copy()
# b[2] = "D"
# print(a)  # {1: 'A', 2: 'B', 3: 'C'}

# # ___________________ задача №36 ___________________
# # Написать программу для слияния нескольких словарей
# dict_a = {1:2, 2:3, 3:4}
# dict_b = {4:5, 5:6, 6:7}
# dict_c = {7:8, 8:9, 9:10}
# # 1й способ
#
# resault = {}
# for i in (dict_a, dict_b, dict_c):
#     resault.update(i)
# # 2й способ
# resault = {**dict_a, **dict_b, **dict_c}

# # ___________________ задача №37 ___________________
# # Выведите все элементы из списка, которые меньше 5
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# # 1й способ
# for elem in a:
#     if elem < 5:
#         print(elem)
#
# # 2й способ
# print(list(filter(lambda elem: elem < 5, a)))
#
# # 3й способ
# print([elem for elem in a if elem < 5])

# # ___________________ задача №38 ___________________
# # Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# # 1й способ
# resault = list(filter(lambda elem: for elem in b, a))
#
# # 2й способ
# resault = [elem for elem in a if elem in b]
#
# # 3й способ
# result = list(set(a) & set(b))  # но при таком способе, не будет повторяющихся элементов, так как кортежи содержат только уникальные элементы

# # ___________________ задача №39 ___________________
# # Отсортировать словарь по возрастанию, и по убыванию
# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#
# # Отсортировать словарь по возрастанию
# resault = dict(sorted(d.items(), key=operator.itemgetter(1)))
# # Отсортировать словарь по убыванию
# resault = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

# # ___________________ задача №40 ___________________
# # Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#
# # 1й способ
# resault = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# # 2й способ при помощи функции nlargest модуля heapq
# from heapq import nlargest
#
# resault = nlargest(3, my_dict, key=my_dict.get)

# # ___________________ задача №41 ___________________
# # написать программу, которая развернет число (тип int)
# # ____  1 способ  ____
# def reverse_number(x):
#     return int(str(x)[::-1])
#
# print (reverse_number(12345))  # 54321
#
# # _____  2 способ  _____
# def reverse_int(x):
#     return int(''.join(list(reversed(str(x)))))
#
# print(reverse_int(12345))  # 54321

# # ___________________ задача №42 ___________________
# # написать программу, которая проверяет является ли число, числом Армстронга.
# # Число Армстронга - натуральное число, которое равно сумме своих цифр, возведенныз в степень, равную количеству его цифр.
# # Например, число 371 = 3**3 + 7**3 + 1**3
# def armstrong_number(num):
#     sum = 0
#     length = len(str(num))
#     for x in list(str(num)):
#        sum += int(x)**length
#     return sum == num
#
# print(armstrong_number(371))  # True
#
# # ___________________ задача №43 ___________________
# # Написать программу, которая проверит каждое число списка, является ли оно простым
# # Простое число - число > 1, у которого есть только два делителя 1 и само число
# def prime_num(num):
#     for x in range(2, num):
#         if num % x == 0:
#             return False
#     return True
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#
# for item in lst:
#     print(f"{item} - {prime_num(item)}")
# 1 - True
# 2 - True
# 3 - True
# 4 - False
# 5 - True
# 6 - False
# 7 - True
# 8 - False
# 9 - False
# 10 - False
# 11 - True
# 12 - False
# 13 - True
# 14 - False


# # ___________________ задача №44 ___________________
# # Написать программу, которая составит список чисел Фибоначчи через итеративный метод.
# # Числа Фибоначчи - последовательность чисел, в которой первые два числа 0, 1, а каждое последующее равно сумме
# # двух предыдущих чисел.
# def fibonacci(length):
#     lst = [0, 1]
#     for item, index in enumerate(range(2, length)):
#         lst.append(lst[index-2] + lst[index - 1])
#     return lst
#
# print(fibonacci(14))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]



# # ************  Практика Stepic Сергей Балакириев  *************
# # ______  Задание 1   ______
# #  С помощью функции print выведите сообщение "Hello Python!" (без кавычек).
# print("Hello Python!")  # Hello Python!

# # ______  Задание 2   ______
# #  С помощью функции print выведите сумму двух чисел 6+7
# print(6 + 7)  # 13

# # ______  Задание 3   ______
# # В программе объявите три следующие переменные с указанными значениями:
# #
# # a = 7
# # b = -4
# # c = 3
# # Выведите в консоль их значения, используя одну функцию print (между значениями переменных должен стоять один пробел).
# a = 7
# b = -4
# c = 3
# print(a, b, c) # 7 -4 3

# # ______  Задание 4   ______
# # В программе объявите три следующие переменные с указанными значениями:
# #
# # a = 7
# # b = -4
# # c = 3
# # Выведите в консоль их значения в столбик (каждое новое значение отображается с новой строчки), используя одну функцию print.
# a = 7
# b = -4
# c = 3
# print(a, b, c, sep="\n")
# # 7
# # -4
# # 3

# # ______  Задание 5   ______
# # В программе объявите две следующие переменные с указанными значениями:
# #
# # s1 = "Hello"
# # s2 = "Balakirev"
# # С помощью двух функций print (каждая отображает соответствующую строку) выведите строки в консоль так, чтобы они шли друг за другом через пробел.
# s1 = "Hello"
# s2 = "Balakirev"
# print(s1, end=" ")
# print(s2)
# # Hello Balakirev

# # ______  Задание 6   ______
# # В программе вводятся строки в переменные s1 и s2. Необходимо их отобразить в консоли в формате:
# #
# # Word 1: s1 | Word 2: s2
# #
# # Например, если s1 = "abc"; s2 = "defsg", то выводится строка:
# #
# # Word 1: abc | Word 2: defsg
# s1, s2 = map(str.strip, input().split())
#
# print(f"Word 1: {s1} | Word 2: {s2}") # Word 1: abc | Word 2: defsg

# # ______  Задание 7   ______
# #  Напишите программу, в которой вводятся (читаются) два целых положительных числа, записанных в одну строчку через пробел, и в консоль выводится результат возведения первого числа в степень второго.
# a, b = map(int, input().split())
# print(a ** b) # 8

# # ______  Задание 8  ______
# # Напишите программу, которая принимает на входе два вещественных числа, записанных в одну строку через пробел, и выводит на экран их сумму.
# a, b = map(float, input().split())
# print(a + b)  # 19.0

# # ______  Задание 9  ______
# # В магазине продается X синих ручек, Y зеленых, черных в два раза больше, чем синих, а красных в четыре раза больше зеленых. Напишите программу, в которой вводятся целые значения X, Y в одну строку через пробел с помощью команды:
# #
# # X, Y = map(int, input().split())
# #
# # и выводится на экран общее число ручек в виде целого числа.
# blue, green = map(int, input().split())
# black = blue * 2
# red = green * 4
# print(blue + black + green + red)  # 130

# # ______  Задание 10  ______
# # На вход программе подаются длина и ширина прямоугольника (вещественные значения, каждое с новой строки). Необходимо прочитать эти значения и вычислить периметр прямоугольника (сумму длин сторон). Результат (периметр) вывести на экран в виде вещественного числа.
# a = float(input())
# b = float(input())
#
# print(float(2 * (a + b)))  # 38.0

# # # ______  Задание 11  ______
# # программе вводится целое число и сохраняется через переменную d. Необходимо продолжить эту программу.
# # Вычислите модуль числа d и выведите результат (модуль) в консоль с помощью функции print.
# d = int(input())
# print(abs(d)) # 5

# # # ______  Задание 12  ______
# #  Допишите текст программы для нахождения минимального значения из пяти введенных целых чисел с выводом результата в
# #  консоль (минимального значения) с помощью функции print.
# d1, d2, d3, d4, d5 = map(int, input().split()) # 1 2 3 4 5
# print(min(d1, d2, d3, d4, d5)) # 5

# # # ______  Задание 13  ______
# # Допишите текст программы для нахождения максимального значения из пяти введенных целых чисел с выводом результата
# # (максимального значения) в консоль с помощью функции print.
# d1, d2, d3, d4, d5 = map(int, input().split())  # 8 11 0 -5 3
# print(max(d1, d2, d3, d4, d5))  # 11

# # # ______  Задание 14  ______
# # Допишите текст программы для вычисления евклидового расстояния (гипотенузы) по перемещениям a и b (формула:___ )
# #Округлите результат с точностью до сотых. Полученное значение выведите на экран.
# a, b = map(int, input().split())  # 3 4
# res = pow(a ** 2 + b ** 2, 0.5)
# print(round(res, 2))  # 5.0

# # # ______  Задание 15  ______
# Допишите программу для нахождения числа сочетаний из n по k (значения вводятся в программе), используя формулу : ____
# # n!=1⋅2⋅⋯⋅n. Выведите результат в консоль в виде целого числа с помощью функции print.
# # Для вычисления факториалов воспользуйтесь соответствующей функцией из библиотеки math.
# import math
# n, k = map(int, input().split())  # 6 3
# print(int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k))))  # 20

# # # ______  Задание 16  ______
# В летний лагерь нужно отвезти n детей и m вожатых с помощью автобусов (значения считываются из входного потока
# в программе ниже). Максимальная вместимость каждого автобуса 20 человек. Допишите программу для вычисления минимального
# числа автобусов, необходимых для перевозки детей вместе с вожатыми. Результат выведите в консоль в виде целого числа.
# import math
# n, m = map(int, input().split())  # 40 5
# print(math.ceil((n + m) / 20)) # 3

# # # ______  Задание 17  ______
# # Гелевая ручка стоит x рублей (значение вводится из входного потока в программе ниже). Сегодня магазин предоставляет
# # скидку в 10% на каждую купленную ручку. Какое наибольшее количество таких ручек можно будет купить на 500 рублей?
# # Результат выведите в консоль в виде целого числа.
# x = int(input())  # 20
# sale = x - (x * 10 / 100)
# print(int(500 // sale))  # 27

# # # ______  Задание 18  ______
# # Напишите программу вывода переменной math.pi с точностью до тысячных (три знака после запятой).
# import math
#
# print(float(f"{math.pi:.3f}"))  # 3.142

# # # ______  Задание 19  ______
# # Составить программу вывода на экран вещественного числа, вводимого с клавиатуры. Выводимому числу должно
# # предшествовать сообщение "Вы ввели число" (без кавычек).
# x = float(input())  # 7.54
# print(f"Вы ввели число {x}")  # Вы ввели число 7.54

# # # ______  Задание 20  ______
# #  Напишите программу, которая из входного потока читает вещественное число. Нужно определить, что целая часть
# #  прочитанного числа кратна 3. На экран вывести True, если кратно и False - в противном случае.
# #  Задача делается без использования условного оператора.
# x = float(input())  # 78.34
# print(int(x) % 3 == 0) # True

# # # ______  Задание 21  ______
# # Напишите программу, которая читает из входного потока стоимость книги X рублей в виде вещественного числа
# # (например, X = 435.78) - положительное вещественное число с точностью до сотых (два знака после запятой).
# # Требуется определить, является ли дробное значение (число после запятой) больше 50. На экран вывести True,
# # если больше и False - в противном случае. Задача делается без использования условного оператора.
# x = float(input())  # 456.56
# print((x * 100) % 100 > 50)  # True

# # # ______  Задание 22  ______
# #  Напишите программу, в которой читаются два целочисленных значения, записанных в одну строчку через пробел, с помощью команды:
# # a, b = map(int, input().split())
# # Необходимо определить, можно ли первое число нацело разделить на второе. На экран вывести True, если делится и False
# # - в противном случае. Задача делается без использования условного оператора.
# a, b = map(int, input().split())  # 12 3
# print(a % b == 0)  # True

# # # ______  Задание 23  ______
# # Напишите программу, в которой читаются три целых положительных числа с помощью команды:
# # a, b, c = map(int, input().split())
# # Необходимо определить, можно ли их интерпретировать (воспринимать) как длины сторон треугольника. Напомню, что сумма
# # длин двух произвольных сторон всегда должна быть больше третьей стороны. На экран вывести True, если треугольник
# # формируется и False - в противном случае. Задача делается без использования условного оператора.
# a, b, c = map(int, input().split())  # 8 11 12
# print((a + b) > c and (a + c) > b and (b + c) > a)  # True

# # # ______  Задание 24  ______
# # Напишите программу, в которой читается вещественное число. Нужно проверить, что прочитанное число попадает или в
# # диапазон [0; 2] или в диапазон [10; 20] (включительно). На экран вывести True, если попадает и False - в противном
# # случае. Задача делается без использования условного оператора.
# x = float(input())  # 1.2
# print(0 <= x <= 2 or 10 <= x <= 20)  # True