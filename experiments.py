
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





