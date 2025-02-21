#______________________  Концепция ООП (Объектно-ориентированное программирование)  _____________________________
# объект - Класс: свойства и методы # Что-то вроде шаблона
# коты:
#     порода
#     кличка
#     возраст
# А уже конкретные коты, это объекты данного класса. Их может быть разное количество
# кот 1(коты):
#    русская
#    Рыжик
#    2
# кот 2(коты):
#    бурма
#    Васька
#    5

# ___________  Инкапсуляция  ______________
# Напрямую к данным и методам класса из вне обращаться нельзя, только внутри класса - такой механизм называется
# инкапсуляцией.

# ___________  Наследование  ______________
# Общие свойства объектов целесообразно вынести в базовый класс. Дочерние классы эти свойства наследуют от
# базового класса.

# ___________  Полиморфизм  ______________
# Возможность работать единым способом с разными типами данных. Методы из базового класса дополнять в дочерних классах

# # ___________________   Классы и объекты классов ____________________
# # class Имя_класса:
# class Point:  # определяем класс, Имя класса принято начинать с заглавной буквы
#     color = "red"  # содержимое класса, например, цвет и радиус точки
#     circle = 2
# # переменные внутри класса чаще называют атрибутами класса или его свойствами
# # класс создает свое пространство имен

# # Чтобы обратиться к его свойствам также используется оператор.
# class Point:
#     color = "red"
#     circle = 2
#
# print(Point.color)  # red
#
# print(Point.__dict__)  # позволяет увидеть все переменные класса
# # {'__module__': '__main__', '__firstlineno__': 37, 'color': 'red', 'circle': 2, '__static_attributes__': (),
# # '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>,
# # '__doc__': None}

# # Чтобы создать экземпляр (объект) класса Имя_класс()
# class Point:
#     color = "red"
#     circle = 2
#
# obj1 = Point()  # создает разные объекты
# obj2 = Point()
# print(id(obj1))  # 2306550819072
# print(id(obj2))  # 2306553498192
#
# print(type(obj1))  # <class '__main__.Point'> тип от класса Point
# #
# # # в самих obj1 и obj2 нет свойств, но они ссылаются на свойства класса Point
# print(obj1.__dict__)  # {}
# print(obj1.color)  # red

# # объекты obj1 также создают свое пространство имен, и обращаясь к их свойствам, мы изменяем их только в этом
# # пространстве, в Point изменений не будет

# class Point:
#     color = "red"
#     circle = 2
#
# obj1 = Point()
# obj1.color = "black"
# print(Point.color)  # red
# print(obj1.color)  # black
# print(obj1.__dict__)  # {'color': 'black'} у этого объекта после присваивания появится свой атрибут

# # Во внешний класс также можно добавлять новые свойства Имя_класса.название_атрибута = значение
# class Point:
#     color = "red"
#     circle = 2
#
# Point.border = ["white", 0.5 ]
# print(Point.__dict__)
# # {'__module__': '__main__', '__firstlineno__': 78, 'color': 'red', 'circle': 2, '__static_attributes__': (),
# # '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>,
# # '__doc__': None, 'border': ['white', 0.5]}

# # или при помощи специального метода setattr(класс, "свойство", значение)
# class Point:
#     color = "red"
#     circle = 2
#
# obj1 = Point()
#
# setattr(obj1, "line_width", 5)
# print(obj1.__dict__)  # {'line_width': 5}
# Если в классе не существует атрибута, которому мы пытаемся присвоить значения, то динамически создается новый

# # getattr(Имя_класса, "атрибут", что вывести, если такого не существует - необязательный параметр) позволяет читать
# # атрибуты из указанного пространства имен, если такого атрибута не  существует, можно задать, что вывести в
# # таком случае
# class Point:
#     color = "red"
#     circle = 2
#
# # getattr(Point, "border")  # AttributeError: type object 'Point' has no attribute 'border'
# a = getattr(Point, "border", False)  # Выведет False, если такого атрибута нет. Чтобы не было ошибки
# b = getattr(Point, "color", False)  # А если такой атрибут есть, то выведет его значение
# print(a)  # False
# print(b)  # red

# # удаление атрибутов
# # 1 способ - del имя_класса.атрибут
# class Point:
#     color = "red"
#     circle = 2
#     border = {'line_width': 5}
#
# del Point.border
# a = getattr(Point, "border", False)
# print(a)  # False атрибут удален
# # повторное удаление атрибута приведет к ошибке, так как нельзя удалять не существующий,
# # проверить наличие атрибута можно при помощи функции hasattr(класс, "атрибут")
# print(hasattr(Point, "border"))  # False

# # 2 способ, при помощи функции delattr(класс, атрибут)
# class Point:
#     color = "red"
#     circle = 2
#     border = {'line_width': 5}
#
# delattr(Point, "border")
# print(hasattr(Point, "border"))  # False

# # функция hasattr() указывает то, что через указанное пространство имен, можно получить доступ к атрибуту, но это
# # не значит, что он находится непосредственно в нем, например
#
# class Point:
#     color = "red"
#     circle = 2
#
# obj1 = Point()
# print(hasattr(obj1, "color"))  #  # на выходе True хотя в самом объекте свойство color не прописано
#
# # а вот удаление происходит именно в текущем пространстве имен
# del obj1.color  # AttributeError: 'Point' object has no attribute 'color' вызовет ошибку

# # Если удалить свойство из объекта класса, то оно унаследуется от родительского класса
# class Point:
#     color = "red"
#     circle = 2
#
# obj1 = Point()
# obj1.color = "black"
# print(obj1.color)  # black
# del obj1.color
# print(obj1.color)  # red

# class Point:
#     "класс точек на координатной плоскости" # можно добавлять описание класса
#     color = "red"
#     circle = 2
#
# print(Point.__doc__)  # метод для вызова описания

# _______________  методы классов _________________
# class:
#     свойства(данные)  # поэтому в названиях методов используют существительные
#     методы (действия)  # поэтому в названиях методов используют глаголы
#
# class Point:
#     color = "red"
#     curcle = 2
#
#
#     def set_coords():
#         print("Вызов метода set_coords")
#
#
# print(Point.set_coords)  # указывает, что атрибут связан с функцией
# # <function Point.set_coords at 0x00000213D9AD37E0>
# # чтобы вызвать метод, необходимо имя_метода()
# print(Point.set_coords())  # Вызов метода set_coords
# Вызов метода set_coords
# None

#
# class Point:
#     color = "red"
#     curcle = 2
#
#
#     def set_coords():
#         print("Вызов метода set_coords")
#
#
# obj = Point()  # создаем экземплар класса
# print(obj.set_coords)  # <bound method Point.set_coords of <__main__.Point object at 0x000001FD2BFB6900>>
# # этот метод связан с классом Point, но при попытке его вызвать возникнет ошибка
# print(obj.set_coords())  # TypeError: Point.set_coords() takes 0 positional arguments but 1 was given
#
#
# # это связано с тем, что при вызове функции передается 1 параметр, а в классе мы задали его без параметров.
# # когда метод вызывается через объект класса, интерпритатор в качестве первого параметра автоматически подставляет
# self (ссылка на экземпляр класса Point)
#
# # чтобы исправить это, необходимо в качестве первого аргумента в классе указать self
# class Point:
#     color = "red"
#     curcle = 2
#
#
#     def set_coords(self):  # этот параметр будет ссылаться на тот экземплар класса, из которого он был вызван
#         print("Вызов метода set_coords " + str(self))  # self это ссылка на экземпляр класса, из которого он вызван
#
#
# obj = Point()
# obj.set_coords()  # Вызов метода set_coords <__main__.Point object at 0x0000023096D56900>

# # но теперь вызов этого метода через класс приведет к ошибке
# Point.set_coords()  # TypeError , так как при вызове мы не указали этот первый параметр self
# # Так как метод вызывается из самого класса, автоматически ничего не подставляется (нет экземплара, для которого вызывается данный метод)
# # если в качестве параметра указать экземпляр, то это будет аналогично записи  obj.set_coords()
# Point.set_coords(obj)  # Вызов метода set_coords <__main__.Point... аналогично obj.set_coords()
#
#
# # чтобы для объекта класса передать свои координаты, используется ссылка на этот объект(self)
# class Point:
#     color = "red"
#     curcle = 2
#
#
#     def set_coords(self, x, y):
#         self.x = x  # создает локальное свойство x для объекта класса, на который ссылается
#         self.y = y  # создает локальное свойство y для объекта класса, на который ссылается
#
#
# obj1 = Point()
# obj2 = Point()
#
# obj1.set_coords(2, 3)  # необходимо при вызове метода передать параметры
# obj2.set_coords(10, 20)
# print(obj1.__dict__)  # {"x" : 2, "y" : 3} # при вызове свойств объекта класса появляются эти заданные свойства
# print(obj2.__dict__)  # {"x" : 10, "y" : 20}

#
# # self нужен для работы с локальными переменными определенного экземпляра класса
#
# # и таких методов может быть в классе несколько
# class Point:
#     color = "red"
#     curcle = 2
#
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def get_coords(self):  # например добавим метод вывода текущих координат
#         return (self.x, self.y)
#
#
# obj = Point()
#
# obj.set_coords(2, 3)
# print(obj.get_coords())  # (2, 3)
#
# # # поскольку методы тоже являются атрибутами, к ним также можно применить специальные функции
# a = getattr(obj, "get_coords")  # так редко вызывают, но это возможно
# print(a)  # <bound method Point.get_coords of <__main__.Point object at 0x0000022E31586900>>
# print(a())  # (2, 3)

# # __________________  инициализатор __init__, финализатор __del__  ______
# # __имя метода __ их называют магическими методами
# # __init__(self) - вызывается сразу после создания экземпляра класса
# # __del__(self) - вызывается непосредственно перед удалением экземпляра класса
# class Point:
#     color = "red"
#     curcle = 2
#
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def get_coords(self):
#         return (self.x, self.y)
#
#
# obj = Point()
# print(obj.__dict__)  # {} локальные переменные не созданы, необходимо вызвать метод
# obj.set_coords(2, 3) # чтобы задать значения у объекта класса, необходимо вызвать метод и затем передать в него значения
# print(obj.__dict__)  # {'x': 2, 'y': 3}

# # Чтобы сделать это сразу, используется метод __init(self)__
# class Point:
#     color = "red"
#     curcle = 2
#
#     def __init__(self):
#         self.x = 0 # создаем локальные свойства с нулевым значением
#         self.y = 0
#
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def get_coords(self):
#         return (self.x, self.y)
#
#
# obj = Point()
# print(obj.__dict__)  # {'x': 0, 'y': 0} Тогда сразу при создании экземпляра класса появятся локальные переменные
#
# если прописать параметры, можно сразу передать значения при создании экземпляра класса
# class Point:
#     color = "red"
#     curcle = 2
#
#     def __init__(self, a, b): # указываем параметры
#         self.x = a
#         self.y = b
#
#
#     def get_coords(self):
#         return (self.x, self.y)
#
#
# obj = Point(5, 7)
# print(obj.__dict__)  # {'x': 5, 'y': 7}

# def __init__(self, x, y): # грамотней указывать параметры с таким же именем, как и атрибуты
#         self.x = x
#         self.y = y
#
# # магические методы это такие же функции, в них также можно прописать формальные параметры (указать значения по умолчанию)
# class Point:
#     color = "red"
#     curcle = 2
#
#     def __init__(self, x=0, y=0): # указываем параметры
#         self.x = x
#         self.y = y
#
#
#     def get_coords(self):
#         return (self.x, self.y)
#
#
# obj1 = Point(5, 7)
# print(obj1.__dict__)  # {'x': 5, 'y': 7}
# obj2 = Point()
# print(obj2.__dict__)  # {'x': 0, 'y': 0} не возникнет ошибки, так как есть значения по умолчанию

#
# class Point:
#     color = "red"
#     curcle = 2
#
#     def __init__(self, x=0, y=0): # указываем параметры
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print(f"удаление класса {str(self)}")
#
#
#     def get_coords(self):
#         return (self.x, self.y)
#
#
# obj1 = Point(5, 7)
# print(obj1.__dict__)  # {'x': 5, 'y': 7}
# # удаление класса <__main__.Point object at 0x000001A81F906900> По завершении программы экземпляр класса будет удален

#______________________  магический метод __new__  ______________________
#__new__() - вызывается перед созданием объекта класса
# если необходима реализация какого-то кода до создания объекта класса
# class Point:
#     def __new__(cls, *args, **kwargs): # cls ссылается на сам класс (Point)
#         print(отработал new")
#
#
#     def __init__(self, x=0, y=0): # self будет ссылаться на создаваемый экземпляр класса
#         self.x = x
#         self.y = y
#         print("отработал init")
#
# pt = Point(1, 2)
# print(pt)
# отработал new
# None - ссылка на pt. Экземпляр класса не был создан

# # метод __new__ должен возвращать адрес созданного экземпляра, эта программа не возвращает
# # чтобы это исправить прописывается такая конструкция super().__new__(cls), то есть вызываем метод new для базового класса
# class Point:
#     def __new__(cls, *args, **kwargs): # cls ссылается на сам класс (Point)
#         print("отработал new")
#         return super().__new__(cls) # super() - ссылка на базовый класс(object), из него вызываем метод new, в который
#         # передаем ссылку на текущий класс (Point)
#
#
#     def __init__(self, x=0, y=0): # self будет ссылаться на создаваемый экземпляр класса
#         self.x = x
#         self.y = y
#         print("отработал init")
#
# pt = Point(1, 2) # эти параметры передаются автоматически в метод new, поэтому чтобы не возникало ошибок
# # необходимо в нем указать список аргументов *args, **kwargs
# print(pt)
# # отработал new
# # отработал init
# # <__main__.Point object at 0x0000021A3E366900>
# # в Python 3 классы наследуются от объекта (object) super() ссылается на него и в нем вызывается магический метод new

# # этот магический метод используется, например, в паттерне проектирования singleton (в примере не полная его реализация)
# # например, необходимо создать класс для работы с базой данных, но так, чтобы существовал только один ее экземпляр
#
# class Data_base:
#     __instance = None # зададим атрибут - ссылка на экземпляр. Если его нет None, а если уже есть, то вернет ссылку на него
#
#     # для управления этим атрибутом переопределим магический метод new
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None: # если экземпляра класса не существует
#             cls.__instance = super().__new__(cls) # то создаем экземпляр
#
#         return cls.__instance # вернуть значение этого атрибута
#
#     def __del__(self):
#         Data_base.__instance = None # при удалении/ завершении вернуть значение None
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def connect(self):
#         print(f"Соединение с БД: user={self.user}, password={self.psw}, port={self.port}")
#
#     def close(self):
#         print("Закрытие соединения с БД")
#
#     def read(self):
#         return "данные из БД"
#
#     def write(self, data):
#         print(f"Запись в БД - {data}")
#
# db = Data_base("root", "1234", 25)
# db2 = Data_base("root2", "1234567", 80)
# print(id(db), id(db2)) #1997018786048 1997018786048 один и тот же id, они ссылаются на один и тот же объект
# db.connect()  # Соединение с БД: user=root2, password=1234567, port=80 - данные те, что передали при попытке
# # создать второй экземпляр
# db2.connect()  # Соединение с БД: user=root2, password=1234567, port=80
# # так как срабатывает init и локальные значения изменяются

# # _____________________________ декораторы @classmethod @staticmethod __________________
# class Vector:
#     min_coords = 0  # атрибуты класса
#     max_coords = 100
#
#     @classmethod # декоратор для метода класса
#     def validate(cls, param): # интегрированная среда подставила cls(ссылка на текущий класс)
#         return cls.min_coords < param < cls.max_coords # вернет True или False. Обращается к атрибутам класса, но
#         # не может обращаться к локальным атрибутам экземпляров класса, так как в функции нет ссылки на него (self)
#
#
#     def __init__(self, x, y): # методы для экземпляров класса
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
# # чтобы вызвать метод можно обратиться к нему через класс
# print(Vector.validate(15)) # True (0 < 15 < 100) # cls передается автоматически
# # а если хотим вызвать метод экземпляра класса, через класс, то ссылку на него необходимо передать
# v = Vector(3, 4)
# print(Vector.get_coords(v))  # (3, 4)

# # делаем проверку x и y, вызвав validate в init
# class Vector:
#     min_coords = 0  # атрибуты класса
#     max_coords = 100
#
#     @classmethod
#     def validate(cls, param):
#         return cls.min_coords < param < cls.max_coords
#
#
#     def __init__(self, x, y):
#         self.x = self.y = 0 # начальные значения
#         # if Vector.validate(x) and Vector.validate(y):  # входят ли x и y в указанный диапазон, если да, то присвоить
#         #     # эти значения
#         #     self.x = x
#         #     self.y = y
#         if self.validate(x) and self.validate(y):  # ссылка на экземпляр класса, также вызовет метод класса, в cls
#             # self передаст ссылку на класс, это более универсальный способ, так как можно переименовать класс,
#             # а код внутри не менять. Поэтому прописывать название класса внутри класса считается плохой практикой
#             self.x = x
#             self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
# v1 = Vector(5, 7)
# v2 = Vector(1, 101)
# print(v1.get_coords()) # (5, 7)
# print(v2.get_coords()) # (0, 0)  # так как условие не выполнилось, новые значения не присвоились, а остались те, что
# # по умолчанию

# статические методы не имеют доступа ни к атрибутам ни к атрибутам его экземпляров - самостоятельная независимая
# # функция внутри класса декоратор @staticmethod
# class Vector:
#     min_coords = 0  # атрибуты класса
#     max_coords = 100
#
#     @classmethod
#     def validate(cls, param):
#         return cls.min_coords < param < cls.max_coords
#
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
#     @staticmethod
#     def norm2(x, y): # вычисление квадратичной нормы вектора # в функции нет никаких скрытых параметров(self, cls)
#         return x * x + y * y
#
# print(Vector.norm2(10, 6))  # 136

# # статическую функцию можно использовать и внутри класса
# class Vector:
#     min_coords = 0  # атрибуты класса
#     max_coords = 100
#
#     @classmethod
#     def validate(cls, param):
#         return cls.min_coords < param < cls.max_coords
#
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
#
#         print(self.norm2(self.x, self.y))
#
#     def get_coords(self):
#         return self.x, self.y
#
#     @staticmethod
#     def norm2(x, y):
#         return x * x + y * y
#
#
# v = Vector(1, 4) # 17

