
# # _____________  практика 1  _____________
# # отображение эмоджи в консоли
# print("\U0001F62A")
# print("\U0001F602")
# print("\U0001F917")
# print("\U0001F637")
# print("\U0001F600")
# print("\U0001F92A")
# print("\U0001F928")
# print("\U0001F605")
# print("\U0001F60D")
#
#
# # 😪
# # 😂
# # 🤗
# # 😷
# # 😀
# # 🤪
# # 🤨
# # 😅
# # 😍

# # _____________  практика 2  _____________
# # отображение квадратной рамки, заданной ширины
# width = int(input("Напишите ширину рамки: "))  # 6
#
# for i in range(width):
#     for j in range(width):
#         if i == 0 or i == width - 1 or j == 0 or j == width - 1:
#             print("*", end="  ")
#         else:
#             print("  ", end=" ")
#     print("\r")
#
# # *  *  *  *  *  *
# # *              *
# # *              *
# # *              *
# # *              *
# # *  *  *  *  *  *

# # _____________  практика 3  _____________
# # рамка - ромб
# num = int(input("Введите число: "))  # 5
#
# for i in range(1, num + 1):
#     for j in range(1, num - i + 1):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# for i in range(num - 1, 0, -1):
#     for j in range(1, num - i + 1):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# #         *
# #       *   *
# #     *       *
# #   *           *
# # *               *
# #   *           *
# #     *       *
# #       *   *
# #         *

# # # _____________  практика 4  _____________
# for i in range(1, 7):
#     print("*" * i)
# for i in range(5, 0, -1):
#     print("*" * i)
# # *
# # **
# # ***
# # ****
# # *****
# # ******
# # *****
# # ****
# # ***
# # **
# # *

# # # # _____________  практика 5  _____________
# from turtle import *
#
# penup() # turtle.penup() — функция модуля turtle языка Python, которая поднимает перо черепахи, в результате чего она
# # не оставляет на холсте след при последующих движениях.
#
# for i in range(42, -1, -1):
#     stamp() # turtle.stamp() — функция из библиотеки turtle языка Python, которая создаёт отпечаток формы черепахи
#     # на холсте в её текущем положении и возвращает ID штампа.
#     left(i)  # turtle.left() — команда модуля Turtle в Python, которая позволяет повернуть черепашку влево на указанный
#     # угол в градусах.
#     forward(28) # turtle.forward() — команда модуля Turtle в Python, которая позволяет переместить «черепашку» вперёд
#     # на указанное число пикселей.
#
#     speed(0) # turtle.speed() — метод модуля turtle в Python, который позволяет изменить скорость черепахи с помощью
#     # значения аргумента.
#
# done()  # turtle.done() — функция модуля turtle в Python, которая приостанавливает выполнение программы до закрытия
# # графического окна.


# # _____________  практика 6  _____________
# from turtle import *
# title('Victoria')
# bgcolor('#511A29')
# pensize(5)
# pencolor('#D49D85')
# lst_name = ["Vika"] * 40
# angle = 360 / 40
# penup()
# sety(-1)
# for _ in range(41):
#     left(angle)
#     forward(260)
#     if lst_name:
#         write(lst_name.pop(), align='center', font=('Arial', 18, 'normal'))
#         backward(260)
#         speed(160)
# penup()
# goto(-20, - 20)
# pendown()
# write('* Victoria *', align='center', font=('Arial', 40, 'normal'))
# hideturtle()
# done()




