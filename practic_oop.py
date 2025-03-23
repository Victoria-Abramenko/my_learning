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

# #___________________  режимы доступа public, private, protected (инкапсуляция)  _____________________
# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#
#
# pt = Point(4, 8)
# print(pt.x, pt.y) # 4 8 # эти свойства доступны извне, через ссылку pt
# # даже можно изменить эти свойства
# pt.x = 20
# pt.y = "Stroke"
# print(pt.x, pt.y)  # 20 Stroke

# чтобы указать доступ к атрибутам класса
# public(публичное свойство) - имя_атрибута без символа одного и двух подчеркиваний вначале атрибута
# protected(обращение внутри его класса и во всех его дочерних классов) - _имя_атрибута с одним символом
# подчеркивания в начале атрибута
# # private(обращение только внутри класса) - __имя_атрибута с двумя символами подчеркивания в начале атрибута

# в режиме protected обращение извне только предупреждает, что подразумевается, что эти атрибуты не должны
# использоваться извне
# class Point:
#     def __init__(self, x = 0, y = 0):
#         self._x = x
#         self._y = y
#
#
# pt = Point(4, 8)
# print(pt._x, pt._y) # 4 8 # По-прежнему можно получить их свойства, но интегрированная среда разработки уже подчеркивает,
# предупреждает, что не стоит использовать извне эти атрибуты, но не ограничивает

# # в режиме private обращение извне приведет к ошибке, но при работе внутри класса проблем не возникнет
# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.__x = x
#         self.__y = y
#
    # def set_coords(self, x, y): # такой метод называется сеттером (получает данные)
    #     if type(x) in (int, float) and type(y) in (int, float): # можно сделать проверку корректности данных
    #         self.__x = x
    #         self.__y = y

#     def get_coords(self):  # такой метод называется геттером
#         return (self.__x, self.__y)
#
# pt = Point(4, 8)
# # print(pt.__x, pt.__y) # AttributeError: 'Point' object has no attribute '__x'
#
# pt.set_coords(10, 11)
# print(pt.get_coords())  # (10, 11) программа отработала без ошибок, внутри класса можно обращаться к этим атрибутам

# интерфейсный метод (сеттер и геттер). Чтобы случайно не нарушить работу класса, с атрибутами стоит взаимодействовать
# через публичные методы(сеттер(установить) и геттер(получить)) - в этом суть инкапсуляции

# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.__x = x
#         self.__y = y
#
#     def set_coords(self, x, y):
#         if type(x) in (int, float) and type(y) in (int, float):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError("координаты должны быть числами") # выведет сообщение ошибки, в случае не соответствия условию
#
#     def get_coords(self):
#         return (self.__x, self.__y)
#
# pt = Point(4, 8)
# pt.set_coords("10", 11)
# print(pt.get_coords())  # ValueError: координаты должны быть числами, в случае передачи неверных данных,
# # выведется указанное сообщение ошибки

# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = self.y = 0 # начальные значения, которые останутся, если переданные аргументы не пройдут проверку
#         # при создании экземпляра класса
#         if self.__check_value(x) and self.__check_value(y): # если пройдут проверку, то атрибуты примут переданное значение
#             self.__x = x
#             self.__y = y
#
#     @classmethod
#     def __check_value(cls, a): # private можно делать и методы класса
#         return type(a) in (int, float) # тогда, чтобы скорректировать проверку, достаточно отредактировать одну строку
#
#     def set_coords(self, x, y):
#         if self.__check_value(x) and self.__check_value(y): # если переданные в метод значения пройдут проверку, то
#             # установятся новые значения
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError("координаты должны быть числами") # если не пройдут, выведется ошибка с этим текстом
#
#     def get_coords(self):
#         return (self.__x, self.__y)
#
# pt = Point(4, 8)
# pt.set_coords(10, 11)
# print(pt.get_coords())

# на самом деле к этим элементам можно обратиться используя их кодовое имя (то, которое указано у экземпляра класса
# в словаре)
# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = self.y = 0
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     @classmethod
#     def __check_value(cls, a):
#         return type(a) in (int, float)
#
#     def set_coords(self, x, y):
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError("координаты должны быть числами")
#
#     def get_coords(self):
#         return (self.__x, self.__y)
#
# pt = Point(4, 8)
# pt.set_coords(10, 11)
# print(pt.__dict__) # {'x': 0, 'y': 0, '_Point__x': 10, '_Point__y': 11} в словаре их имя _Point__x и _Point__y
# print(pt._Point__x, pt._Point__y) # 10 11 по этому имени они доступны извне, хоть среда разработки и предупреждает,
# # программа отработает - но так делать не рекомендуется

# Чтобы строже защитить атрибуты можно использовать специальный модуль accessify, но его сначала необходимо установить
# pip install accessify

# # from accessify import private, protected # декораторы для методов
# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = self.y = 0
#         if self.check_value(x) and self.check_value(y):
#             self.__x = x
#             self.__y = y
#
#     # @private
#     @classmethod
#     def check_value(cls, a):
#         return type(a) in (int, float)
#
#     def set_coords(self, x, y):
#         if self.check_value(x) and self.check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError("координаты должны быть числами")
#
#     def get_coords(self):
#         return (self.__x, self.__y)
#
# pt = Point(4, 8)
# pt.set_coords(10, 11)
# pt.check_value(5) # при декораторе @private выведет ошибку, что данный метод является приватным
# # защита с этим модулем более надежная, но чаще используют два подчеркивания, так как этого достаточно

# # ____________  магические методы __setattr __getattr  _________________________
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
# 
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# 
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
# 
# pt1 = Point(1, 2)
# pt3 = Point(3, 4)
#
# # если в пространстве имен не существует какого-то атрибута(явно не указан в экземпляре класса), то поиск переходит
# # во внешнее пространство имен (атрибуты в самом классе)
# # print(pt1.MAX_COORDS) # 100
#
# # чтобы обратиться к атрибутам класса внутри метода, также необходимо указать ссылку на класс(использовать лучше self,
# # а не имя класса)
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS: # ссылка на класс через self
#             self.x = x
#             self.y = y
#
# # но чтобы изменить атрибут внутри класс, есть нюанс
#     def set_bound(self, left):
#         self.MIN_COORDS = left # здесь оператор присваивания создаст этот атрибут с новым значением в текущей локальной
#         # области видимости(в экземпляре класса, а не изменит значение самого класса)
#
# pt1 = Point(1, 2)
# pt1.set_bound(50)
# print(pt1.__dict__) # {'x': 1, 'y': 2, 'MIN_COORDS': 50} атрибуты экземпляра класса pt1
# print(Point.__dict__) # {'__module__': '__main__', '__firstlineno__': 754, 'MIN_COORDS': 0, 'MAX_COORDS': 100,
# # '__init__': <function Point.__init__ at 0x0000015DBE0137E0>,
# # 'set_coords': <function Point.set_coords at 0x0000015DBE013920>,
# # 'set_bound': <function Point.set_bound at 0x0000015DBE0139C0>,
# # '__static_attributes__': ('MIN_COORDS', 'x', 'y'), '__dict__': <attribute '__dict__' of 'Point' objects>,
# # '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None}
# # значение 'MIN_COORDS': 0 у класса Point осталось прежним
#
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
# # но чтобы изменить атрибут внутри класса, нужно использовать декоратор (метод класса) и ссылку на сам класс cls
#     @classmethod
#     def set_bound(cls, left):
#         cls.MIN_COORDS = left #
#
# pt1 = Point(1, 2)
# pt1.set_bound(50)
# print(pt1.__dict__) # {'x': 1, 'y': 2} не создается новый атрибут в экземпляре класса pt1
# print(Point.__dict__)# ...'MIN_COORDS': 50,... а в самом классе изменилось значение этого атрибута, хотя вызывали этот
# # метод через экземпляр класса

# __setattr__(self, key, value) - автоматически вызывается при изменении свойств key класса
# __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item
# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса
# __delattr__(self, item) - автоматически вызывается при удалении свойства item (независимо от того существует оно или нет)

# метод __getattribute__(self, item)
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     def __getattribute__(self, item):
#         print("автоматически вызвался __getattribute__ при считывании атрибута через экземпляр класса")
#         return object.__getattribute__(self, item)  # чтобы этот метод отработал корректно необходимо обратиться
#         # к общему object, от которого неявно наследуются все классы. Передаем ему те же параметры, поскольку метод
#         # должен возвращать значение атрибута используем return
#
# pt = Point(1, 2)
# a = pt.x # обращение к атрибуту через экземпляр класса, при запуске программы отработает метод __getattribute__
# print(a)
# # автоматически вызвался __getattribute__ при считывании атрибута через экземпляр класса
# # 1 - возвращает значение атрибута
# # None если закомментировать строчку return в __getattribute__, то значение будет None

# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     def __getattribute__(self, item): # такой метод используется, например, если необходимо закрыть доступ к атрибуту
#         if item == "x": # если обращение будет к x, выведется ошибка
#             raise ValueError("Доступ к x ограничен")
#         else:
#             return object.__getattribute__(self, item) # если обращение будет не к x, то вернется его значение
#
# pt = Point(1, 2)
# a = pt.x # ValueError: Доступ к x ограничен
# print(a)

# метод __setattr__(self, key, value)
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     def __setattr__(self, key, value): # автоматически вызывается, когда идет присвоение какому-либо атрибуту значения
#         # key - имя атрибута, value - значение, которое присваивается
#         print("автоматически вызвался __setattr__ при присвоении значений атрибуту через экземпляр класса")
#
# pt = Point(1, 2) # передаются 2 значения, поэтому при запуске программы, метод __setattr__ отработает дважды
# # автоматически вызвался __setattr__ при присвоении значений атрибуту через экземпляр класса
# # автоматически вызвался __setattr__ при присвоении значений атрибуту через экземпляр класса
#
# # этот метод можно использовать, чтобы запретить создавать новый атрибут
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     def __setattr__(self, key, value):
#         if key == "z": # если мы попытаемся создать атрибут z выведет ошибку
#             raise AttributeError("недопустимое имя атрибута")
#         else: # при создании любого другого просто присвоит ему значение
#             object.__setattr__(self, key, value)
#
# pt = Point(1, 2)
# pt.z = 3 # AttributeError: недопустимое имя атрибута

# # у этого атрибута есть еще нюанс, если присваивать в нем значение атрибуту через self, то он будет отрабатывать
# # по рекурсии и упадет с ошибкой
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     def __setattr__(self, key, value):
#         if key == "z": # если мы попытаемся создать атрибут z выведет ошибку
#             raise AttributeError("недопустимое имя атрибута")
#         else: # при создании любого другого просто присвоит ему значение
#             self.x = value
#
# pt = Point(1, 2)
# pt.i = 5
# # RecursionError: maximum recursion depth exceeded

# # чтобы исправить это, необходимо обратиться к коллекции атрибутов(__dict__) через ключ
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     def __setattr__(self, key, value):
#         if key == "z": # если мы попытаемся создать атрибут z выведет ошибку
#             raise AttributeError("недопустимое имя атрибута")
#         else: # при создании любого другого просто присвоит ему значение
#             self.__dict__[key] = value # но лучше это делать через object
#
# pt = Point(1, 2)
# pt.i = 5
# # тогда ошибки не возникнет

# метод __getattr__
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     def __getattr__(self, item): # автоматически вызывается при обращении к несуществующему атрибуту экземпляра класса
#         print("автоматически вызвался __getattr__ при обращении к несуществующему атрибуту")
#
# pt = Point(1, 5)
# print(pt.yy)
# автоматически вызвался __getattr__ при обращении к несуществующему атрибуту
# None

# # его используют, например, чтобы вернуть значение False, вместо возврата исключения(ошибки)
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     def __getattr__(self, item): # при запуске программы без этого метода, в случае обращения к несуществующему
#         # атрибуту возникла бы ошибка
#         return False
#
# pt = Point(1, 5)
# print(pt.yy) # False и никакой ошибки

# # метод __delattr__
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     def __delattr__(self, item): # автоматически вызывается при удалении атрибута
#         print(f"автоматически вызвался __delattr__ так как удалили атрибут {item}")
#
# pt = Point(1, 5)
# del pt.x # автоматически вызвался __delattr__ так как удалили атрибут x
# # но сам атрибут удален не будет
# print(pt.__dict__) # {'x': 1, 'y': 5}

# # чтобы удалить этот атрибут, его снова нужно вызвать через object
# class Point:
#     MIN_COORDS = 0
#     MAX_COORDS = 100
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         if self.MIN_COORDS < x < self.MAX_COORDS and self.MIN_COORDS < y < self.MAX_COORDS:
#             self.x = x
#             self.y = y
#
#     def __delattr__(self, item): # автоматически вызывается при удалении атрибута экземпляра класса
#         print(f"автоматически вызвался __delattr__ так как удалили атрибут {item}")
#         object.__delattr__(self, item)
#
# pt = Point(1, 5)
# del pt.x # автоматически вызвался __delattr__ так как удалили атрибут x
# print(pt.__dict__) # {'y': 5} # теперь атрибут удален

# # ________________  паттерн моносостояния __________________________
# # через этот паттерн реализуется, что все экземпляры класса имеют единые локальные атрибуты. Изменение этих атрибутов
# # в одном экземпляре, отражается изменениями их и в других экземплярах
#
# class Thread_data: # создаем приватный атрибут, в котором будут общие локальные атрибуты экземпляров класса, в виде словаря
#     __shares_attr = {
#         "name" : "thread1",
#         "data" : {},
#         "id" : 1
#     }
#
# # __dict__ ссылается на словарь с локальными данными экземпляра класса
#
#     def __init__(self):
#         self.__dict__ = self.__shares_attr # у каждого экземпляра класса коллекция __dict__ будет ссылаться на __shares_attr
#
# th1 = Thread_data() # автоматически свойства __shares_attr появляются у каждого созданного экземпляра
# th2 = Thread_data()
# print(th1.__dict__)
# print(th2.__dict__)
# # {'name': 'thread1', 'data': {}, 'id': 1}
# # {'name': 'thread1', 'data': {}, 'id': 1}
# th2.id = 3 # значение id изменится не только в th2, но и в th1
# print(th1.__dict__)
# print(th2.__dict__)
# # {'name': 'thread1', 'data': {}, 'id': 3}
# # {'name': 'thread1', 'data': {}, 'id': 3}
# th1.attr_new = "new" # и создание нового локального свойства также отобразится в других экземплярах
# print(th1.__dict__)
# print(th2.__dict__)
# # {'name': 'thread1', 'data': {}, 'id': 3, 'attr_new': 'new'}
# # {'name': 'thread1', 'data': {}, 'id': 3, 'attr_new': 'new'}

# #________________  декоратор @property  ____________________
# # используется для работы с приватными атрибутами
# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     # для работы с приватными свойствами необходимо написать сеттеры и геттеры - публичные методы, для
#     # работы с приватными свойствами
#     def get_old(self):
#         return self.__old
#
#     def set_old(self, old):
#         self.__old = old
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
# p1 = Person("Vika", 33)
# p1.set_old(34)
# print(p1.get_old()) # 34
# # таким способом получается, что для каждого атрибута надо прописать свой сеттер и геттер

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     # для работы с приватными свойствами необходимо написать сеттеры и геттеры - публичные методы, для
#     # работы с приватными свойствами
#     def get_old(self):
#         return self.__old
#
#     def set_old(self, old):
#         self.__old = old
#
#     old = property(get_old, set_old) # создаем экземпляр объекта property(геттер, сеттер)
# # когда идет вызов атрибута old(property)автоматически вызывается геттер, а при передаче значения сеттер
# p1 = Person("Vika", 33)
# a = p1.old
# print(a)  # 33
# p1.old = 35
# print(p1.old)  # 35
# print(p1.__dict__)  # {'_Person__name': 'Vika', '_Person__old': 35} # при этом в локальном пространстве этого свойства
# # old нет
# # атрибут = property имеет высокий приоритет, и даже если в экземпляре класса будет атрибут old, вызываться будет
# # именно этот атрибут

# чтобы убедиться в этом, искусственно создадим локальное свойство old, через __dict__
# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     def get_old(self):
#         return self.__old
#
#     def set_old(self, old):
#         self.__old = old
#
#     old = property(get_old, set_old)
#
# p1 = Person("Vika", 33)
# p1.__dict__['old'] = "локальное свойство"
# p1.old = 35 # обращение к свойству property, а не к созданной локальной переменной
# print(p1.old) # все равно выводит 35
# print(p1.__dict__) # {'_Person__name': 'Vika', '_Person__old': 35, 'old': 'локальное свойство'} при этом это
# локальное свойство существует

# # если атрибут будет обычным, то приоритет наоборот у локальных свойств, сначала используется локальное свойство
# экземпляра класса, а если его нет, тогда свойство самого класса
# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     def get_old(self):
#         return self.__old
#
#     def set_old(self, old):
#         self.__old = old
#
#     old = 5
#
# p1 = Person("Vika", 33)
# p1.__dict__['old'] = "локальное свойство"
# print(p1.old) # локальное свойство
# print(p1.__dict__) # {'_Person__name': 'Vika', '_Person__old': 33, 'old': 'локальное свойство'}

# свойство property удобно тем, что не надо запоминать названия все геттеров и сеттеров
# у класса property есть методы setter(), getter, deleter() - это декораторы, которые можно использовать при создании
# объекта свойства
# можно записать используя эти декораторы
# old = property()
# old = old.getter(get_old)
# old = old.setter(set_old)
# также отработает, поэтому методы класса можно переписать иначе

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property # декоратор property прописывается перед геттером
#     def old(self):
#         return self.__old
#
#     @old.setter # а перед сеттером уже через @get_old (стало объектом Property) вызов декоратора сеттер
#     def old(self, old): # !!! но необходимо переименовать метод, чтобы он также назывался
#         self.__old = old
#
#     @old.deleter
#     def old(self):
#         del self.__old
# #
# p1 = Person("Vika", 33)
# p1.old = 35 # методы теперь оба называются get_old (как было с примером old)
# print(p1.old) # 35 новое значение установилось и вывелось, только без отдельного выноса property
# # вот так чаще всего на практике и используют
# del p1.old # удаление __old
# print(p1.__dict__) # {'_Person__name': 'Vika'} свойство удалено

# _____________ пример использования объектов property ________________

# Person ФИО, возраст (от 14 до 55), серия номер паспорта (в формате xxxx xxxxxx), где x целое число

# от 0 до 9, вес в кг от 20 и больше - вещественное число

# ФИО - список из 3 строк

# возраст - целое число

# паспорт - строка в нужном формате

# вес - вещественное число
# _____________  пример использования объектов property  ________________
# Person ФИО, возраст (от 14 до 55), серия номер паспорта (в формате xxxx xxxxxx), где x целое число
# от 0 до 9, вес в кг от 20 и больше - вещественное число
# ФИО - список из 3 строк
# возраст - целое число
# паспорт - строка в нужном формате
# вес - вещественное число
#
# from string import ascii_letters
# class Person:
#     S_RUS = "абвгдежзиклмнопрстуфхцчщъыьэюя"
#     S_RUS_UPPER = S_RUS.upper()
#
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio) # если этот метод отработает без ошибок, то программа пойдет дальше
#         self.verify_old(old)
#         self.verify_passport(ps)
#         self.verify_weight(weight)
#
#         self.__fio = fio.split()  # разбиваем строку на строки
#         self.__old = old
#         self.__passport = ps
#         self.__weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if type(fio) != str:  # проверка, чтобы данные были строкой
#             raise ValueError("Некоррекные данные")
#
#         fio_list = fio.split()
#         if len(fio_list ) != 3:  # проверяем чтобы в списке была и фамилия и имя и отчество
#             raise ValueError("Неверный формат записи")
#
#         # создаем вспомогательную переменную, которая будет содержать список допустимых символов
#         # ascii_letters набор латинских букв малых и больших
#         # cls.S_RUS набор руских букв
#         # cls.S_RUS_UPPER набор русских заглавных букв
#         letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
#
#         for elem in fio_list:
#             if len(elem ) < 1:
#                 raise TypeError("Должен быть хотя бы 1 символ")
#             if len(elem .strip(letters)) != 0: # проверка на допустимые символы
#                 raise TypeError("Содержаться недопустимые символы")
#             # реализация через len - если допустимый символ, то сработает метод strip, который удалит
#             # этот символ, а значит длина = 0
#
#     @classmethod
#     def verify_old(cls, old):
#         if type(old) != int or old < 14 or old > 55:
#             raise TypeError("Неверно указан возраст")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if type(w) != float or w < 20:
#             raise TypeError("Вес указан не корректно")
#
#     @classmethod
#     def verify_passport(cls, ps):
#         if type(ps) != str:
#             raise TipeError("Не является строкой")
#
#         s = ps.split() # деление строки по пробелу (список из 2 элементов, в 1й строке 4 символа, во второй 6
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#
#         for i in s:
#             if not i.isdigit():  # проверка на цифры
#                 raise TypeError("Указаны не цифры")
# # Затем все эти методы необходимо вызвать перед атрибутами, чтобы провести проверку до их присвоения
#
#     @property
#     def fio(self):  # создаем геттер для работы с фио, причем сеттер необязательно задавать, если не планируется изменение
#         return self.__fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old  # прежде чем присвоить новое значение, следует сделать проверку
#
#     @property
#     def passport(self):
#         return self.__passport
#
#     @passport.setter
#     def passport(self, ps):
#         self.verify_passport(ps)
#         self.__passport = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
# p1 = Person("Иванов Иван Иванович", 30, "1234 567890", 75.3)
# p1.old = 33
# p1.weight = 120.0
# print(p1.__dict__)
# # {'_Person__fio': ['Иванов', 'Иван', 'Иванович'], '_Person__old': 33, '_Person__passport': '1234 567890', '_Person__weight': 120.0}
# print(p1.passport)  # 1234 567890

# поскольку мы опредили геттер, можно переписать атрибуты (все кроме fio, так как ему мы не написали сеттер)

# from string import ascii_letters
# class Person:
#     S_RUS = "абвгдежзиклмнопрстуфхцчщъыьэюя"
#     S_RUS_UPPER = S_RUS.upper()
#
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio) # остальные проверка запустится из геттера
#
#         self.__fio = fio.split()
#         self.old = old  # присваиваем методы
#         self.passport = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if type(fio) != str:  # проверка, чтобы данные были строкой
#             raise ValueError("Некоррекные данные")
#
#         fio_list = fio.split()
#         if len(fio_list ) != 3:  # проверяем чтобы в списке была и фамилия и имя и отчество
#             raise ValueError("Неверный формат записи")
#
#         letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
#
#         for elem in fio_list:
#             if len(elem ) < 1:
#                 raise TypeError("Должен быть хотя бы 1 символ")
#             if len(elem .strip(letters)) != 0:
#                 raise TypeError("Содержаться недопустимые символы")
#
#     @classmethod
#     def verify_old(cls, old):
#         if type(old) != int or old < 14 or old > 55:
#             raise TypeError("Неверно указан возраст")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if type(w) != float or w < 20:
#             raise TypeError("Вес указан не корректно")
#
#     @classmethod
#     def verify_passport(cls, ps):
#         if type(ps) != str:
#             raise TipeError("Не является строкой")
#
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#
#         for i in s:
#             if not i.isdigit():  # проверка на цифры
#                 raise TypeError("Указаны не цифры")
#
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def passport(self):
#         return self.__passport
#
#     @passport.setter
#     def passport(self, ps):
#         self.verify_passport(ps)
#         self.__passport = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
# p1 = Person("Иванов Иван Иванович", 30, "1234 567890", 75.3)
# p1.old = 33
# p1.weight = 120.0
# print(p1.__dict__)
# # {'_Person__fio': ['Иванов', 'Иван', 'Иванович'], '_Person__old': 33, '_Person__passport': '1234 567890', '_Person__weight': 120.0}
# print(p1.passport)  # 1234 567890

# у объектов свойств есть недостаток - повторение кода для каждого атрибута
# class Point3d:
#     # def __init__(self, x, y, z):
#     #     self._x = x
#     #     self._y = y
#     #     self._z = z
#     # так как мы прописали сеттеры и геттеры(_x...), в инициализаторе можно просто присвоить методы.
#
#     def __init__(self, x, y, z): # при такой записи будет срабатывать соответсвующий сеттер
#         self.x = x
#         self.y = y
#         self.z = z
#
#     @classmethod
#     def verify_coord(cls, coord):
#         if type(coord) != int:
#             raise TypeError("Координата должна быть целым числом")
#
#     @property
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, coord):
#         self.verify_coord(coord) # проводим проверку, и только потом присваиваем
#         self._x = coord
#
#     @property
#     def y(self):
#         return self._y
#
#     @y.setter
#     def y(self, coord):
#         self.verify_coord(coord)
#         self._y = coord
#
#     @property
#     def z(self):
#         return self._z
#
#     @z.setter
#     def z(self, coord):
#         self.verify_coord(coord)
#         self._z = coord
#
# p = Point3d(1, 2, 3)
# print(p.__dict__) # {'_x': 1, '_y': 2, '_z': 3} локальные переменные созданы без ошибок

# с этой проблемой помогут дескрипторы
# ____________________  Дескрипторы  _________________
# дескриптор - класс, который содержит магический метод
# class A __get__ - дескриптор не данных (non-data descriptor)
# class B __get__ + __set__ и / или  __del__ - дескриптор данных (data descriptor)
# создаем дескриптор(класс), а затем создать его экземпляры в классе Point - x = Integer(), y = Integer(), x = Integer()
# __get__(self<ссылка на экземпляр этого дескриптора>, instance<на экземпляр класса>, owner<ссылка на класс>)
# __set_name__(self<ссылка на экземпляр этого дескриптора>, owner <ссылка на класс>, name <имя, которому присваивается экземпляр дескриптора>)
#__set__(self<ссылка на экземпляр этого дескриптора>, instance<ссылка на экземпляр класса>, value<значение>)
# благодаря параметрам сеттеры и геттеры реализованы универсальным способом

# # в момент создания в классе экземпляров дескриптора запускается метод __set_name__
# # в момент срабатывания инициализатора(т.е при создании экземпляра класса) срабатывает сеттер (__set__)
# # при обращении через экземпляр класса к атрибуту срабатывает геттер (__get__)
# class Integer_point:
#     @classmethod  # метод проверки также перенесем в класс Integer_point
#     def verify_coord(cls, coord):
#         if type(coord) != int:
#             raise TypeError("Координата должна быть целым числом")
#
#     def __set_name__(self, owner, name): # для формирования локального свойства, к которому потом будем обращаться
#         self.name = "_" + name # x = _x
#
#     def __set__(self, instance, value):
#         self.verify_coord(value) # проверяем значение, прежде чем его присвоить
#         instance.__dict__[self.name] = value # p1.__dict__[self._x] = 1, p1.__dict__[self._y] = 2, p1.__dict__[self._z] = 3
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name] # return p1.__dict__[self._x], return p1.__dict__[self._y], return p1.__dict__[self._z]
#
# class Point3d:
#     x = Integer_point() # формируем дескрипторы для взаимодействия с координаторами
#     y = Integer_point()
#     z = Integer_point()
#
#     def __init__(self, x, y, z): # Этим дескрипторам присваиваем значения(имя координаты), срабатавает метод __set_name__,
#         # в результате переменные получаться с подчеркиванием
#         self.x = x # _x | self.x это первый экземпляр Integer_point
#         self.y = y # _y | self.y это второй экземпляр Integer_point
#         self.z = z # _z | self.z это третий экземпляр Integer_point
#
#     # @classmethod # метод проверки также перенесем в класс Integer_point
#     # def verify_coord(cls, coord):
#     #     if type(coord) != int:
#     #         raise TypeError("Координата должна быть целым числом")
#
# p1 = Point3d(1, 2, 3)
# print(p1.__dict__) # {'_x': 1, '_y': 2, '_z': 3}
# # p2 = Point3d(1.1, 2, 3) # TypeError: Координата должна быть целым числом - проверка сработала

# в дескрипторе также можно упростить код, используя специальные функции setattr и getattr, это более правильный способ
# class Integer_point:
#     @classmethod
#     def verify_coord(cls, coord):
#         if type(coord) != int:
#             raise TypeError("Координата должна быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name # x = _x
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         setattr(instance, self.name, value) # getattr(<область видимости объекта>, <название этого атрибута>, <значение>
#         # которое хотим присвоить)
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)  # для работы с локальными переменными getattr(<область видимости объекта>
#         # из которого хотим взять аргумент, <название этого атрибута> которое хранится в self.name)
#
# class Point3d:
#     x = Integer_point()
#     y = Integer_point()
#     z = Integer_point()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
#
# p1 = Point3d(1, 2, 3)
# print(p1.__dict__)  # {'_x': 1, '_y': 2, '_z': 3}
# это дескриптор данных - на его основе мы создали координаты

# # дескриптор не данных - они могут только считывать данные, плюс приоритет считывания такой же как у атрибутов класса
# # добавим такой дескриптор в нашу программу
# class Read_x: # создаем класс не данных
#     def __set_name__(self, owner, name):
#         self.name = "_x" # метод именно для чтения x, поэтому локальная переменная _x
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
# class Integer_point:
#     @classmethod
#     def verify_coord(cls, coord):
#         if type(coord) != int:
#             raise TypeError("Координата должна быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name # x = _x
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         setattr(instance, self.name, value) # getattr(<область видимости объекта>, <название этого атрибута>, <значение>
#         # которое хотим присвоить)
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)  # для работы с локальными переменными getattr(<область видимости объекта>
#         # из которого хотим взять аргумент, <название этого атрибута> которое хранится в self.name)
#
# class Point3d:
#     x = Integer_point()
#     y = Integer_point()
#     z = Integer_point()
#     xr = Read_x() # это дескриптор не данных
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
#
# p1 = Point3d(1, 2, 3)
# print(p1.xr)  # 1
# # но при присвоении другого значения ошибки не возникнет, а создастся новая переменная с этим значением
# p1.xr = 5
# print(p1.__dict__) # {'_x': 1, '_y': 2, '_z': 3, 'xr': 5}
# # То есть мы просто создали локальный атрибут xr, словно дескриптора xr нет
# # а вот у  дескриптора данных приоритет выше
# # но в целом на практике используется редко

# магические методы еще называют - dunder-методы (от англ. double underscope двлйное почеркивание)

# # ______________________  магический метод __call__  ______________________
# # на примере класса счетчика
# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
# c = Counter() # __call__ автоматически запускается при вызове класса Class_name()

# # в этом методе, сначала вызывается __new__, затем __init__
# # упрощенная схема реализации метода
# # def __call__(self, *args, **kwargs):
# #     obj = self.__new__(self, *args, **kwargs)
# #     self.__init__(obj, *args, **kwargs)
# #     return obj
# # благодаря этому методу класс можно вызывать, как функцию(), а вот экземпляр класса, так уже вызвать нельзя,
# # это приведет к ошибке
#
# c() # TypeError: 'Counter' object is not callable
# так как в них не определен магический метод __call__

# # можно прописать метод для экземплчров класса. Например, подсчет вызовов
# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         return self.__counter
#
# c = Counter()
# c2 = Counter() # второй экземпляр класса. Оба счетчика будут независимы друг от друга
# c() # не приведет к ошибке
# c()
# c2()
# res = c()
# res2 = c2()
# print(res) #  3
# print(res2) #  2
# # у счетчиков разные значения, не зависимые друг от друга
# # экземпляры классов, которые можно вызывать подобно функциям называются функторы
#
# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, step=1, *args, **kwargs): # можно прописывать дополнительные аргументы, например величину шага
#         self.__counter += step
#         return self.__counter
#
# c = Counter()
# c2 = Counter()
# c()
# c(2)
# c2(3)
# res = c(2)
# res2 = c2(3)
# print(res)  # 5
# print(res2)  # 6

# # Где применяется - например, класс удаления определенных символов в конце строки, вместо использования замыкания функции
# class Strip_chars:
#     def __init__(self, chars): # здесь сохраним коллекцию символов, которые будем удалять в строке
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str): # проверяем, что переданный элемент является строкой, если нет вывести исключение
#             raise TypeError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.__chars) # возвращаем строку с удаленными символами
#
# s1 = Strip_chars(" !#$%^&?.*,")
# s2 = Strip_chars(" ")# создаем экземпляр класса и передаем в него символы для удаления
# res = s1("*** hello world! ***")  # вызываем этот экземляр класса и передеем внего строку, у которой хотим удалить символы
# res2 = s2("*** hello world! ***")  # этот экземляр отработает независимо от первого даже если передать ту же строку
#
# print(res, res2, sep="\n")
# # hello world
# # *** hello world! ***

# # как второй пример, в качестве реализации декоратора
# import math
#
# class Derivate:
#     def __init__(self, func): # здесь передаем функцию, функционал которой будем расширять
#         self.__fn = func
#
#     def __call__(self, x, dx = 0.0001, *args, **kwargs): # в качестве аргументов переменную, для которой будем вычислять производную,
#     # и шаг производной
#         return (self.__fn(x + dx) - self.__fn(x)) / dx
#
# def df_sin(x):  # для функции синуса
#     return math.sin(x)
#
# print(df_sin(math.pi / 3 # 0.8660254037844386 вычисляем синус от числа pi / 3

# # применить класс в качестве декоратора можно двумя способами:
# # 1й способ
# import math
#
# class Derivate:
#     def __init__(self, func):
#         self.__fn = func
#
#     def __call__(self, x, dx = 0.0001, *args, **kwargs):
#         return (self.__fn(x + dx) - self.__fn(x)) / dx
#
# def df_sin(x):
#     return math.sin(x)
#
# df_sin = Derivate(df_sin)  # функции присваиваем класс, с ссылкой на эту функцию (df_sin - стала экземпляром класса Derivate)
# print(df_sin(math.pi / 3)) # 0.4999566978958203
#
# # 2й способ
# import math
#
# class Derivate:
#     def __init__(self, func):
#         self.__fn = func
#
#     def __call__(self, x, dx = 0.0001, *args, **kwargs):
#         return (self.__fn(x + dx) - self.__fn(x)) / dx
#
# @Derivate
# def df_sin(x):
#     return math.sin(x)
#
# print(df_sin(math.pi / 3))  # 0.4999566978958203

# _________________  dunder методы  ____________________
# каждый магический метод автоматически срабатывает в определенный момент
# __str__() в момент отображения информации (для пользователей - в print, str)
# __repr__() в момент отображения информации (для разработчиков - в режиме отладки)
# class Cats:
#     def __init__(self, name):
#         self.name = name
#
# cat1 = Cats("Васька")
# print(cat1) # <__main__.Cats object at 0x0000028B1AF66900> # отобразится такая информация при использовании print для
# экземпляра класса

# # При помощи магического метода __repr__ можно изменить вид отображения информации
# class Cats:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"экземпляр класса {self.__class__}, имя кота в данном экземпляре {self.name} "
#
# cat1 = Cats("Васька")
# print(cat1) # экземпляр класса <class '__main__.Cats'>, имя кота в данном экземпляре Васька - вид отображения
# # информации изменился

# # При этом, если написать метод __str__, то уже не будет срабатывать __repr__ так как для вывода информации
# # для пользователей запускается автоматически
# class Cats:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"экземпляр класса {self.__class__}, имя кота в данном экземпляре {self.name} "
#
#     def __str__(self):
#         return f"вариант отображения для пользователей - Имя: {self.name}"
#
# cat1 = Cats("Васька")
# print(cat1)  # вариант отображения для пользователей - Имя: Васька>

# но если запустить просто cat в python console, то сработает __repr__
# экземпляр класса <class '__main__.Cats'>, имя кота в данном экземпляре Васька

# # __len__ - позволяет применять функцию len() к экземпляру класса - автоматически запускается при вызове функции len()
# # __abs__ - позволяет применять функцию abs() к экземпляру класса - автоматически запускается при вызове функции abs()
# class Point:
#     def __init__(self, *args):
#         self.__coords = args  # список из координат точек
#
# p1 = Point(1, 2, 3)
# print(len(p1))  # TypeError: object of type 'Point' has no len() - попытка применить функцию к экземпляру класса
# # приведет к ошибке

# # чтобы это исправить, необходимо определить метод __len__
# class Point:
#     def __init__(self, *args):
#         self.__coords = args  # список из координат точек
#
#     def __len__(self):
#         return len(self.__coords)  # указываем для чего именно она применяется
#
# p1 = Point(1, 2, 3)
# print(len(p1))  # 3 функция отработала без ошибки
#
# class Point:
#     def __init__(self, *args):
#         self.__coords = args  # список из координат точек
#
#     def __abs__(self):
#         return list(map(abs, self.__coords)) # вычисление модуля для каждого элемента коллекции
#
# p1 = Point(1, 2, -3)
# print(abs(p1)) # [1, 2, 3]

# #_________________  магические методы арифметических операций  _______________________
# # __add__ - для операции сложения
# # __sub__ - для операции вычитания
# # __mul__ - для операции умножения
# # __truediv__ - для операции деления
# class Clock:
#     __Day = 86400  # максимальное количество секунд в дне
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__Day
#
#     def get_time(self):
#         s = self.seconds % 60  # текущее число секунд
#         m = (self.seconds // 60) % 60  # текущее число минут (self.seconds // 60 - минуты) (% 60 - отбрасываем те минуты, которые уйдут в часы)
#         h = (self.seconds // 3600) % 24  #  текущее число часов (self.seconds // 3600) - количество сек в часе (% 24 так как в сутках 24 часа)
#         return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}" # вернем отформатированную при помощи метода строку
#
#     @classmethod
#     def __get_formated(cls, x):
#         return str(x).rjust(2, "0") # число преобразуем в строку и добавляем незначащие нули (вначале)
#         # если будет число 7, то строка 07
#
# c1 = Clock(3546) # создаем экземпляр класса с количеством секунд
# # print(c1.get_time())  # 00:59:06
# # если, например, необходимо увеличить время
# c1.seconds = c1.seconds + 30
# print(c1.get_time())  # 00:59:36
#
# # чтобы это можно было записать работая только с экземплярами класса c1 = c1 + 30 (не обращаясь к конкретному атрибуту),
# # необходимо в класс добавить магический метод:
# # __truediv__ - для операции деления
# class Clock:
#     __Day = 86400  # максимальное количество секунд в дне
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__Day
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"
#
#     @classmethod
#     def __get_formated(cls, x):
#         return str(x).rjust(2, "0")
#
#     def __add__(self, other):  # other то значение, на которое хотим изменить
#         if not isinstance(other, int):
#             raise ArithmeticError("Прибавлять можно только целые числа")
#         return Clock(self.seconds + other)# возвращаем новый экземпляр класса с новым количеством секунд
#
# c1 = Clock(3546)
# c1 = c1 + 30  # c1.__add__(30)
# print(c1.get_time()) # 00:59:36

# можно также реализовать, чтобы вторым операндом также был экземпляр класса
# class Clock:
#     __Day = 86400  # максимальное количество секунд в дне
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__Day
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"
#
#     @classmethod
#     def __get_formated(cls, x):
#         return str(x).rjust(2, "0")
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError("Прибавлять можно только целые числа или класс Clock")
#
#         st = other
#         if isinstance(other, Clock): # если в метод передается класс, то ссылается на seconds
#             st = other.seconds
#         return Clock(self.seconds + st) # если передаем число, то сложение будет с числом, а если класс, то с его секундами
#
# # c1 = Clock(3546)
# # c2 = Clock(2278)
# # c3 = c1 + c2  # c1.__add__(c2)
# # print(c3.get_time())  # 01:37:04

# # даже если добавить еще экземпляр класса этот метод отработает, так как сложение будет выполняться последовательно
# c1 = Clock(3546)
# c2 = Clock(2278)
# c3 = Clock(3451)
# c4 = c1 + c2 + c3 # c1.__add__(c2) -> временная_переменная = Clock(5824) -> временная_переменная .__add__(c3)
# print(c4.get_time())  # 02:34:35

# порядок записи имеет значение, так как 
# c1 = Clock(3546)
# c1 = 30  + c1 # приведет к ошибке, так как в этом случае __add__ вызывается для Int
# print(c1.get_time())  # TypeError: unsupported operand type(s) for +: 'int' and 'Clock'

# # для такого случая есть магический метод __radd__, но он работает с методом __add__
# class Clock:
#     __Day = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__Day
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"
#
#     @classmethod
#     def __get_formated(cls, x):
#         return str(x).rjust(2, "0")
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError("Прибавлять можно только целые числа или класс Clock")
#
#         st = other
#         if isinstance(other, Clock):
#             st = other.seconds
#         return Clock(self.seconds + st)
#
#     def __radd__(self, other):
#         return self + other # self = c1, other = 30 -> c1 + 30 -> c1.__add__(30)
#
#     def __iadd__(self, other): # срабатывает при +=
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError("Прибавлять можно только целые числа или класс Clock")
#
#         st = other
#         if isinstance(other, Clock):
#             st = self.seconds
#
#         self.seconds += st
#         return self
#
#
# # c1 = Clock(3546)
# # c1 = 30 + c1 # метод __radd__ срабатывает для экземпляра класса, расположенного справа
# # print(c1.get_time())  # 00:59:36
#
# # для сокращенного варианта += используется __iadd__
# c1 = Clock(3546)
# c1 += 30  # если не прописать метод __iadd__, то создастся новый экземпляр класса
# print(c1.get_time())

# по аналогии используются другие магические методы
# оператор | метод
# x + y | __add__(self, other)
# x - y | __sub__(self, other)
# x * y | __mul__(self, other)
# x / y | __truediv__(self, other)
# x // y | __floordiv__(self, other)
# x % y | __mod__(self, other)

# # ____________  магические методы сравнения  ___________
# # __eq__() | ==
# # __ne__() | !=
# # __lt__() | <
# # __le__() | <=
# # __gt__() | >
# # __ge__() | =>
# class Clock:
#     __Day = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__Day
#
# c1 = Clock(1000)
# c2 = Clock(1000)
# print(c1 == c2)  # False так сравниваются id экземпляров классов, а они разные, чтобы сравнить время, которое они хранят,
# # необходимо переписать магический метод

# class Clock:
#     __Day = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__Day
#
#     def __eq__(self, other): # вызовится при сравнении ==
#         if not isinstance(other, (int, Clock)):  # делаем проверку, что вторым аргументов будет либо целое число, либо экземпляр класса
#             raise TypeError("Сравнивать можно только с целым числом или экземпляром класса")
#
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds == sc
#
# c1 = Clock(1000)
# c2 = Clock(1000)
# print(c1 == c2) # True
# print(c1 == 1000) # True
# print(c1 == 2000)  # False
# # при этом сравнение на неравенство отрабатывает, хотя магический метод в классе не прописан
# print(c1 != 5000)  # True в этом случае выполняется not(c1 == c2), если не переопределить метод __ne__()
# print(c1 != 1000) # False
# # а сравнение на больше или меньше уже выдаст ошибку, если не переопределить магический метод
# print(c1 > c2)  # TypeError: '>' not supported between instances of 'Clock' and 'Clock'

# class Clock:
#     __Day = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__Day
#
#     def __eq__(self, other): # вызовится при сравнении ==
#         if not isinstance(other, (int, Clock)):  # делаем проверку, что вторым аргументов будет либо целое число, либо экземпляр класса
#             raise TypeError("Сравнивать можно только с целым числом или экземпляром класса")
#
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds == sc
#
#     def __gt__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError("Сравнивать можно только с целым числом или экземпляром класса")
#
#         g = otger if isinstance(other, int) else other.seconds
#         return self.seconds > g
#
# c1 = Clock(1000)
# c2 = Clock(2000)
# print(c1 > c2)  # False
# print(c1 < c2)  # True так как python заменит это на c2 > c1 и сравнит их, даже без переопределения магического метода

# но так дублируется код, чтобы исправить это, необходимо повторяющиеся строки вынести в отдельный метод
# class Clock:
#     __Day = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__Day
#
#     @classmethod
#     def __verify_data(cls, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError("Сравнивать можно только с целым числом или экземпляром класса")
#
#         return other if isinstance(other, int) else other.seconds
#
#
#     def __eq__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds == sc
#
#     def __gt__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds > sc
#
# c1 = Clock(1000)
# c2 = Clock(2000)
# print(c1 > c2)  # False
# print(c1 < c2)  # True

# # сравнение на >= Или <=
# class Clock:
#     __Day = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__Day
#
#     @classmethod
#     def __verify_data(cls, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError("Сравнивать можно только с целым числом или экземпляром класса")
#
#         return other if isinstance(other, int) else other.seconds
#
#
#     def __eq__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds == sc
#
#     def __gt__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds > sc
#
#     def __le__(self, other):
#         sc = self.__verify_data(other)
#         return self.seconds <= sc
#
# c1 = Clock(1000)
# c2 = Clock(2000)
# print(c1 >= c2)  # False, здесь по такому же принципу, просто операнды переставляются местами и идет проверка на <=
# print(c1 <= c2)  # True

# ___________  функция hash() и хэши объектов  __________
# # hash для определенного объекта всегда одинаковый. Используется только для неизменяемых объектов, с изменяемыми
# вызовет ошибку TypeError: unhashable type: 'list'

# print(hash("python"))  # 6786681493828827225
# print(hash("python"))  # 6786681493828827225
# print(hash(123))  # 123
# print(hash((1, 2, 3)))  # 529344067295497451
# print(hash([1, 2, 3])) # TypeError: unhashable type: 'list'
# # а наоборот - одинаковый хэш не означает, что объекты будут одинаковыми, хотя это бывает редко, но это возможно

# если объекты равны a == b, то и их хэши равны
# если хэши равны hash(a) == hask(b), это не всегда значит, что объекты тоже равны
# если хэши не равны hash(a) != hash(b), то и объекты не равны

# некоторые объекты в python используют хэш, например словари, используют хэши в качестве своих ключей.
# в словарях в качестве ключей можно использовать только неизменяемые типы.
# когда добавляем ключ со значением в словарь, автоматически образуется кортеж (хэш ключа, ключ),
# так как при поиске в словаре по специальному алгоритму находится по хэшу (в случае нахождения одинаковых хэшей, уже
# сравниваются ключи), благодаря такому подходу значения в словаре находятся быстрее

# # при работе с классом
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p1 = Point(1, 2)
# p2 = Point(1, 2)
#
# print(hash(p1), hash(p2), sep=" | ")  # 168049829520 | 168050058385 эти объекты воспринимаются, как неизменяемые,
# # поэтому для них можно вычислять хэш
# print(p1 == p2)  # False не равны, поэтому и хэши разные, но

# # если переписать магический метод для равенства (чтобы объекты считались равными, если у них равны координаты), то
# # появится ошибка TypeError: unhashable type: 'Point', так как перестает работать стандартный алгоритм вычисления хэша.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
# p1 = Point(1, 2)
# p2 = Point(1, 2)
#
# print(hash(p1), hash(p2), sep=" | ")
# print(p1 == p2)

# # чтобы все снова работало, необходимо переопределить магический метод __hash()__
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash((self.x, self.y))  # хэш определяем от координат точек (кортеж с коортдинатами)
#
# p1 = Point(1, 2)
# p2 = Point(1, 2)
#
# print(hash(p1), hash(p2), sep=" | ")   # -3550055125485641917 | -3550055125485641917 причем теперь хэши одинаковые
# print(p1 == p2)   # True
#
# # например создадим словарь и передадим объекты в качестве ключа
# d = {}
# d[p1] = 1
# d[p2] = 2
# print(d) # {<__main__.Point object at 0x0000020D07616900>: 2} в качестве ключа объект, а значение перезаписалось, так как
# # хэш одинаковый, и воспринимается как один и тот же ключ

# ___________________  функция bool() и магические методы  _____________________
# # если не определен магический метод __bool__, то вызывается __len__, при использовании функции bool()
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p1 = Point(3, 4)
# print(bool(p1))  # True при применении функции к пользовательскому объекту практически всегда будет True,

# # чтобы изменить это, необходимо либо переопределить магический метод __len__ либо __bool__
# # __len__
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __len__(self):
#         # возвращаем квадрат длины и радиус вектора
#         return self.x * self.x + self.y * self.y
#
# #
# # p1 = Point(3, 4)
# # print(len(p1))  # 25
# # print(bool(p1))  # True bool(25)
#
# p1 = Point(0, 0)
# print(len(p1))  # 0
# print(bool(p1))  # False

# # __bool__
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __len__(self): # этот метод уже не отработает при вызове bool(), а только при вызове len()
#         return self.x * self.x + self.y * self.y
#
#     def __bool__(self): # при вызове функции bool() приоритет будет у магического метода __bool__
#         return self.x == self.y  # для примера если координаты точки равны, True
#
# p1 = Point(3, 4)
# print(len(p1))  # 25
# print(bool(p1))  # False так как x != y
#
# p1 = Point(0, 0)
# print(len(p1))  # 0
# print(bool(p1)) # True так как x == y
# # магический метод __bool__ всегда должен возвращать либо True либо False, другие значения не допустимы
#
# # чаще функция bool() с объектами не вызывается явно, а в условных операторах
# if p1:
#     print("Координаты точек равны") # Координаты точек равны
# else:
#     print("Координаты точек не равны")

# # _______________ магические методы __getitem__, __setitem__, __delitem__  __________________
# # __getitem__(self, item) - получение значения по ключу
# # __setitem__(self,key, item) - запись значения по ключу
# # __delitem__(self, key) - удаление по ключу
# # на примере класса Студентов (имя и его оценки)
# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
# student1 = Students("Григорий", [4, 4, 3, 3, 5, 4])
# print(student1.marks[2])   # 3

# # если мы хотим обращаться к оценкам, используя только экземпляр класса, необходимо переопределить метод __getitem__
# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):  # [2] передается в item
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Такого индекса в списке нет")
#
# student1 = Students("Григорий", [4, 4, 3, 3, 5, 4])
# print(student1[2]) # 3

# # если необходимо изменить значение, обращаясь к экземпляру класса, то необходимо переопределить магический метод __setitem__
# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):  # [2] передается в item
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Такого индекса в списке нет")
#
#     def __setitem__(self, key, value):  # [2] - key, 4 - value
#         if not isinstance(key, int) or key < 0: # можем прописать свои условия, например, чтобы индексы были только положительными
#             raise TypeError("индекс должен быть целым и не отрицательным числом")
#         self.marks[key] = value
#
# student1 = Students("Григорий", [4, 4, 3, 3, 5, 4])
# student1[2] = 4
# print(student1[2])  # 4


# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):  # [2] передается в item
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Такого индекса в списке нет")
#
#     def __setitem__(self, key, value):  # можно расширить функционал, например, если индекс будет больше длины списка,
#         # заполнить его элементами по умолчанию
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("индекс должен быть целым и не отрицательным числом")
#
#         # сверка на длины списка и индекса
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks) # разница между длиной списка и задаваемым индексом
#             self.marks.extend([None] * off) # расширяем / заполняем список значением None до необходимого индекса
#
#         self.marks[key] = value # затем присваиваем новое значение по индексу
#
#
# student1 = Students("Григорий", [4, 4, 3, 3, 5, 4])
# student1[2] = 4
# print(student1.marks)  # 4
# student1[7] = 5
# print(student1.marks)  # [4, 4, 4, 3, 5, 4, None, 5]

# # если необходимо удалить элемент, нужно переопределить магический метод __delitem__
# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):  # [2] передается в item
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Такого индекса в списке нет")
#
#     def __setitem__(self, key, value):  # можно расширить функционал, например, если индекс будет больше длины списка,
#         # заполнить его элементами по умолчанию
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("индекс должен быть целым и не отрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("индекс должен быть целым числом")
#         del self.marks[key]
#
#
# student1 = Students("Григорий", [4, 4, 3, 3, 5, 4])
# del student1[6]  # удаление None
# print(student1.marks) # [4, 4, 3, 3, 5, 4]

# # __________________  магические методы __iter__ и __next__  __________________
# # __iter__(self) - получение итератора для перебора объекта
# # __next__(self) - переход к следующему значению и его считыванию
# # it1 = iter(lst) - функционал для перебора элементов, next(it1) переходит к следующему значению
# # функция range(start, atop, step) - итератор (арифметическая последовательность)
# # как это работает (механизм перебора любого оператора) на примере функции range
# a = iter(range(5))
# print(next(a))  # 0
# print(next(a))  # 1
# print(next(a))  # 2
# print(next(a))  # 3
# print(next(a))  # 4

# class Float_range:
#     def __init__(self, start = 0.0, stop = 0.0, step = 1.0):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.value = self.start - self.step # определим начальное значение value
#         # (чтобы первое значение self.value + self.step было равно self.start)
#
#     def __next__(self):
#         if self.value + self.step < self.stop:  # проверка, если текущее значение + шаг меньше значения стоп, то
#             self.value += self.step  # прибавляем шаг и сохраняем это значение
#             return self.value  # возвращаем это новое значение
#         else:
#             raise StopIteration # в ином случае генерируем исключение стоп итерация
#
# fr1 = Float_range(0, 2, 0.5)
# # print(fr1.__next__()) # 0.0
# # print(fr1.__next__()) # 0.5
# # print(fr1.__next__()) # 1.0
# # print(fr1.__next__()) # 1.5

# # благодаря магическому методу __next__ можно использовать функцию next
# print(next(fr1)) # 0.0
# print(next(fr1)) # 0.5
# print(next(fr1)) # 1.0
# print(next(fr1)) # 1.5

# # fr1 получается итерируемый объект, но если его перебрать через цикл for, возникнет ошибка , так как не применяется
# # функция iter к fr1
# class Float_range:
#     def __init__(self, start = 0.0, stop = 0.0, step = 1.0):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.value = self.start - self.step
#
#     def __next__(self):
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
#
# fr1 = Float_range(0, 2, 0.5)
# for i in fr1:
#     print(i) # TypeError: 'Float_range' object is not iterable

# # чтобы это исправить необходимо прописать магический метод __iter__
# class Float_range:
#     def __init__(self, start = 0.0, stop = 0.0, step = 1.0):
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#
#     def __iter__(self):
#         self.value = self.start - self.step # перенесем в этот метод определение value
#         return self # вернуть сам объект, так как он и является итератором
#
#     def __next__(self):
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
#
# fr1 = Float_range(0, 2, 0.5)
# for i in fr1:
#     print(i)
# # 0.0
# # 0.5
# # 1.0
# # 1.5
#
# # добавим класс Fr2d для формирования таблицы значений
# class Float_range:
#     def __init__(self, start = 0.0, stop = 0.0, step = 1.0):
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#
#     def __iter__(self):
#         self.value = self.start - self.step # перенесем в этот метод определение value
#         return self # вернуть сам объект, так как он и является итератором
#
#     def __next__(self):
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
#
# class Fr2d:
#     def __init__(self, start = 0.0, stop = 0.0, step = 1.0, rows = 5):
#         self.rows = rows
#         self.fr = Float_range(start, stop, step) # этот экземпляр класса будет формировать числа для каждой строки
#
#     # для того, чтобы обходить элементы, делаем из класса итератор
#     def __iter__(self):
#         self.value = 0
#         return self
#
#     def __next__(self):
#         if self.value < self.rows: # еще не все строки пройдены
#             self.value += 1 # увеличим значение на 1
#             return iter(self.fr)  # возвращаем итератор этого объекта
#         else:
#             raise StopIteration
#
# fr = Fr2d(0, 2, 0.5, 3)
# for row in fr:  # здесь в качестве значения получаем итератор iter(self.fr)
#     for column in row:  # здесь перебираем итератор Float_range(start, stop, step)  и получаем конкретные значения
#         print(column, end=" ")  # для отображения значений через пробел
#     print()  # для переноса на новую строку
# # 0.0 0.5 1.0 1.5
# # 0.0 0.5 1.0 1.5
# # 0.0 0.5 1.0 1.5

# # _____________  наследование классов  _______________________
# # Если необходимо, чтобы атрибуты одного класса были доступны в другом классе, используется наследование
# class Geom:
#     name = "Geom"

#
# class Line:
#     def draw(self):
#         print("Рисуется линия")
#
# g = Geom()
# l = Line()
# # Если в данном случае через экземпляр класса l обратиться к атрибуту name возникнет ошибка, так как Geom Line два
# # разных класса. А значит и два разных пространства имен
# print(l.name)  # AttributeError: 'Line' object has no attribute 'name'

# # чтобы атрибуты класса сделать доступными для другого класса, его необходимо указать в скобках
# class Geom:
#     name = "Geom"

#
# class Line(Geom):
#     def draw(self):
#         print("Рисуется линия")

#
# g = Geom()
# l = Line()
# # тогда этот атрибут станет доступен
# print(l.name)  # Geom
#
# # Когда один класс определяется на основе другого называется наследованием
# # Geom в данном случае базовый (родительский) класс
# # Line подкласс (дочерний класс)

# # наследование помогает избежать дублирования кода
# class Geom:
#     name = "Geom"

#
# class Line(Geom):
#     def draw(self):
#         print("Рисуется линия")
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2

#
# class Rect(Geom): # класс для рисования прямоугольника
#     def draw(self):
#         print("Рисуется прямоугольник")
#
#     def set_coords(self, x1, y1, x2, y2): # получается дублирование кода
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2

# # чтобы это исправить можно перенести повторяющийся код в родительский класс
# class Geom:
#     name = "Geom"
#
#     def set_coords(self, x1, y1, x2, y2): # параметр self в базовом классе может ссылаться не только на класс,
#         # но и на объекты дочернего класса Line и Rect, если вызывается из объектов дочерних классов
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2

#
# class Line(Geom):
#     def draw(self):
#         print("Рисуется линия")
#
#
#
# class Rect(Geom): # класс для рисования прямоугольника
#     def draw(self):
#         print("Рисуется прямоугольник")

#
# l = Line()
# r = Rect()
# l.set_coords(1, 1, 2, 2)
# r.set_coords(3, 3, 4, 4)
# # поскольку оба класса наследуются от Geom можно обратиться к методу set_coords и передать координаты
# print(l.__dict__)  # {'x1': 1, 'y1': 1, 'x2': 2, 'y2': 2}
# print(r.__dict__)  # {'x1': 3, 'y1': 3, 'x2': 4, 'y2': 4}

# # Если указать метод draw в базовом классе, то при вызове из объекта дочернего класса этот метод отработает, так как
# # self будет ссылаться на line
# class Geom:
#     name = "Geom"
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.draw()

#
# class Line(Geom):
#     def draw(self):
#         print("Рисуется линия")

#
# class Rect(Geom):
#     def draw(self):
#         print("Рисуется прямоугольник")

#
# l = Line()
# r = Rect()
# g = Geom ()
# l.set_coords(1, 1, 2, 2) # Рисуется линия
# r.set_coords(3, 3, 4, 4) # Рисуется прямоугольник
# # но при этом если вызвать через базовый класс, будет ошибка, так как в нем нет draw (так как self ссылается Geom)
# g.set_coords(0, 0, 0, 0) # AttributeError: 'Geom' object has no attribute 'draw'
# Поэтому не стоит прописывать в базовом классе метод, определенный в дочерних классах

# # ______________________  функция issubclass()  _________________________________
# class Geom:
#     pass
#
# # print(Geom.__name__) # выведется атрибут name, хотя в самом классе он никак не реализован, это связано с тем что класс
# # # наследуется от object, у которого есть все эти параметры
# g = Geom()
# print(g) # <__main__.Geom object at 0x00000212568A6900> при работе вызове функции print сработал магический
# # метод __str__ в классе object

# class Geom: # этот класс наследуется от object (class Geom(object))
#     pass
#
# class Line(Geom): # этот класс уже наследуется от Geom, а не напрямую от object, но он также имеет доступ ко всем
#     # атрибутам класса object
#     pass
#
# # функция issubclass() позволяет определить является ли класс подклассом другого класса. issubclass(дочерний класс,
# # базовый класс)
# l = Line()
# print(issubclass(Line, Geom))  # True, так как Line является дочерним классом класса Geom
# print(issubclass(Line, object))  # True, так как Line является дочерним классом класса object
# print(issubclass(Geom, Line))  # False, так как Geom не наследуется от Line
#
# # в качестве аргументов можно передавать классы, но не их экземпляры, это приведет к ошибке
# # print(issubclass(l, Geom)) # TypeError: issubclass() arg 1 must be a class
#
# # если необходимо проверить экземпляр класса, следует использовать функцию isinstance(она может работать как с классами,
# # так и с объектами классов)
# print(isinstance(l, Geom))  # True
#
# # типы данных в python так же являются классами и также наследуются от object
# print(isinstance(int, object)) # True

# # можно создать класс, который будет наследоваться от стандартного класса (list), и в нем переопределить отображение значений
# class New_list(list):  # наследуется от list, а значит в качестве параметров будет список
#     def __str__(self):  # этот метод срабатывает при использовании функции print
#         return " ".join(map(str, self)) # здесь параметр self это передаваемый список
#         # отображение значений будет через пробел, одна общая строка
#
# n = New_list([1, 2, 3])
# print(n)  # 1 2 3 теперь отображается так, а не как по умолчанию [1, 2, 3] стандартный вывод списка


#________________  функция super()  ___________
# # Когда дочерний элемент наследуется от базового класса, и в нем прописывается какой-либо метод(параметр) - это
# # называется расширением базового класса
# class Geom:
#     name = "Geom"
#
#
# class Line(Geom):
#     def draw(self):  # расширение базового класса (extended)
#         print("Рисование линии")
#
# # Когда дочерний элемент наследуется от базового класса, и в базовом классе тоже есть такой метод(параметр) - то это
# # называется переопределением
# class Geom:
#     name = "Geom"
#
#     def draw(self):
#         print("Рисование геометрии")
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")  # переопределение (overriding)

# class Geom:
#     name = "Geom"
#
#     def __init__(self):
#         print("Сработал инициализатор Geom")
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# l = Line()  # Сработал инициализатор Geom

# class Geom:
#     name = "Geom"
#
#     def __init__(self):
#         print("Сработал инициализатор Geom")
#
#
# class Line(Geom):
#     def __init__(self):
#         print("Сработал инициализатор Line")
#
#     def draw(self):
#         print("Рисование линии")
#
#
# l = Line()  # Сработал инициализатор Line

# class Geom:
#     name = "Geom"
#
#     def __init__(self):
#         print("Сработал инициализатор Geom")
#
#
# class Line(Geom):
#
#
#     def __init__(self, x1,y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     def draw(self):
#         print("Рисование линии")
#
#
# l = Line(0, 0, 10, 20)
# print(l.__dict__)  # {'x1': 0, 'y1': 0, 'x2': 10, 'y2': 20}

# но если мы будем создавать несколько дочерних классов, будет дублирование кода
# class Geom:
#     name = "Geom"
#
#     def __init__(self):
#         print("Сработал инициализатор Geom")
#
#
# class Line(Geom):
#     def __init__(self, x1,y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     def draw(self):
#         print("Рисование линии")
#
# class Rect(Geom):
#     def __init__(self, x1,y1, x2, y2, fill=None):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.fill = fill
#
#     def draw(self):
#         print("Рисование прямоугольника")
#
#
# l = Line(0, 0, 10, 20)

# # чтобы избежать дублирование кода, выносим сточки в базовый класс
# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Сработал инициализатор для {self.__class__}")
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         print("сработал Rect init")
#         self.fill = fill
#
#     def draw(self):
#         print("Рисование прямоугольника")
#
#
# l = Line(0, 0, 10, 20)  # Сработал инициализатор для <class '__main__.Line'>
# r = Rect(1, 2, 3, 4) # сработал Rect init
#
# # Но чтобы создать локальный свойства координат в дочернем классе Rect, необходимо также вызвать init базового класса,
# # но при нахождении такого метода в дочернем классе, дальнейший поиск прекращается, поэтому он не вызывается,
# # чтобы это исправить.

# # 1 способ - прописать(вызвать его напрямую)
# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Сработал инициализатор для {self.__class__}")
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         Geom.__init__(self, x1, y1, x2, y2)  # вызывает инициализатор базового класса
#         print("сработал Rect init")
#         self.fill = fill
#
#     def draw(self):
#         print("Рисование прямоугольника")
#
#
# l = Line(0, 0, 10, 20)
# r = Rect(1, 2, 3, 4)
# # Сработал инициализатор для <class '__main__.Line'>
# # Сработал инициализатор для <class '__main__.Rect'>  # а значит он был запущен
# # сработал Rect init

# # но это не лучшая практика, так как потенциально могут быть проблемы, при переименовании классов
# # Лучше использовать специальную функцию (возвращает ссылку на объект посредник)
# # 2 способ
# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Сработал инициализатор для {self.__class__}")
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         super().__init__(x1, y1, x2, y2)  # возвращает ссылку на объект-посредник, через который вызываются методы
#         # базового класса, поэтому здесь self не нужен
#         print("сработал Rect init")
#         self.fill = fill
#
#     def draw(self):
#         print("Рисование прямоугольника")
#
#
# l = Line(0, 0, 10, 20)
# r = Rect(1, 2, 3, 4)
# # Сработал инициализатор для <class '__main__.Line'>
# # Сработал инициализатор для <class '__main__.Rect'>  # а значит он был запущен
# # сработал Rect init

# инициализатор класса необходимо прописывать в первую очередь, иначе он может поменять локально свойств, так как стоит после
# вызов методов класса через функцию super - называется делегированием

# ________________________   Режимы доступа ______________________________
# attribute режим доступа public
# _attribute режим доступа protected
# __attribute режим доступа private
# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Сработал инициализатор для {self.__class__}")
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         super().__init__(x1, y1, x2, y2)
#         self.__fill = fill
#
#
# r = Rect(0, 0, 10, 10)
# print(r.__dict__)
# Сработал инициализатор для <class '__main__.Rect'>
# {'_Geom__x1': 0, '_Geom__y1': 0, '_Geom__x2': 10, '_Geom__y2': 10, '_Rect__fill': None}
# в том классе, в котором прописан приватный атрибут, тот префикс и прописывается _Geom__y1 и _Rect__fill
#
# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Сработал инициализатор для {self.__class__}")
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         super().__init__(x1, y1, x2, y2)
#         self.__fill = fill
#
#     def get_coords(self): # если поместить этот метод в класс Rect, то его вызов выдаст ошибку
#         return (self.__x1, self.__y1)
#
# r = Rect(0, 0, 10, 10)
# r.get_coords() # выдаст ошибку, так как атрибуты приватные
# print(r.__dict__)
# # AttributeError: 'Rect' object has no attribute '_Rect__x1'. Did you mean: '_Geom__x1'?

# то есть эти атрибуты доступны только внутри класса, даже в дочерних классах они не доступны
# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Сработал инициализатор для {self.__class__}")
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def get_coords(self): # если поместить этот метод в класс Geom, все отработает без ошибок
#         return (self.__x1, self.__y1)
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         super().__init__(x1, y1, x2, y2)
#         self.__fill = fill
#
#
# r = Rect(0, 0, 10, 10)
# r.get_coords()
# print(r.__dict__)

# # чтобы атрибуты были доступны и в дочерних классах, необходимо использовать режим protected
# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Сработал инициализатор для {self.__class__}")
#         self._x1 = x1
#         self._y1 = y1
#         self._x2 = x2
#         self._y2 = y2
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         super().__init__(x1, y1, x2, y2)
#         self._fill = fill
#
#     def get_coords(self):
#         return (self._x1, self._y1)
#
# r = Rect(0, 0, 10, 10)
# r.get_coords() # отработает без ошибок, так как атрибуты в режиме protected
# print(r.__dict__)

# # приватными можно сделать и методы
# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Сработал инициализатор для {self.__class__}")
#         self.__verify_coords(x1) # если вызвать этот метод в классе, никаких ошибок не будет
#         self._x1 = x1
#         self._y1 = y1
#         self._x2 = x2
#         self._y2 = y2
#
#     def __verify_coords(self, coord):  # Создаем приватный метод
#         return 0 <= coord <= 100
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         super().__init__(x1, y1, x2, y2)
#         self._fill = fill
#
#     def get_coords(self):
#         return (self._x1, self._y1)
#
# r = Rect(0, 0, 10, 10)
# r.get_coords() # отработает без ошибок, так как метод вызван в самом классе
# print(r.__dict__)

# # но если попытаться вызвать метод в дочернем классе, выведется ошибка
# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Сработал инициализатор для {self.__class__}")
#         self._x1 = x1
#         self._y1 = y1
#         self._x2 = x2
#         self._y2 = y2
#
#     def __verify_coords(self, coord):  # Создаем приватный метод
#         return 0 <= coord <= 100
#
#
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         self.__verify_coords(x1)  # если вызвать этот метод в дочернем классе, произойдет ошибка
#         super().__init__(x1, y1, x2, y2)
#         self._fill = fill
#
#     def get_coords(self):
#         return (self._x1, self._y1)
#
#
#
# r = Rect(0, 0, 10, 10)
# r.get_coords()
# print(r.__dict__)
# # AttributeError: 'Rect' object has no attribute '_Rect__verify_coords'. Did you mean: '_Geom__verify_coords'?

# ______________________  Полиморфизм  _____________________
# # Полиморфизм - возможность работать с разными объектами единым образом (через единый интерфейс)
# # На примере двух классов, прямоугольник и квадрат, в которых есть геттер на получение периметров этих фигур
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_rect_per(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_sq_per(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# print(r1.get_rect_per(), r2.get_rect_per())  # 6 14
# print(s1.get_sq_per(), s2.get_sq_per())  # 40 80

# # Если для удобства поместить объекты в список, а затем пройтись циклом по ним, чтобы применить к ним геттер, то не выйдет,
# # так как каждой фигуры свой метод (с разными названиями)
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_rect_per(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_sq_per(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
#
# geom = [r1, r2, s1, s2]
# for i in geom:
#     # print(i.get_sq_per()) но для квадрата один метод
#     # print(i.get_rect_per()) для прямоугольника другой
#     print(i.get_sq_per()) # поэтому возникнет ошибка
# # AttributeError: 'Rectangle' object has no attribute 'get_sq_per'. Did you mean: 'get_rect_per'?

# # эту проблему можно решить 2 способами:
# # 1 при помощи условного оператора (не лучший выбор)
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_rect_per(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_sq_per(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
#
# geom = [r1, r2, s1, s2]
# for i in geom:
#     if isinstance(i, Rectangle): # Если прямоугольник, то этот метод
#         print(i.get_rect_per())
#     else: # Если квадрат, то этот метод
#         print(i.get_sq_per()) # но если добавится еще объект(к примеру, треугольник, программа опять выдаст ошибку)
# # 6
# # 14
# # 40
# # 80

# # используя принцип полиморфизма
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_per(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
#
# geom = [r1, r2, s1, s2]
# for i in geom:
#     print(i.get_per()) # одинаковое название методов. Для каждого объекта вызовется свой метод
# # 6
# # 14
# # 40
# # 80

# # список можно сформировать иначе(сразу создавать в нем экземпляры классов)
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_per(self):
#         return 4 * self.a
#
# geom = [
#     Rectangle(1, 2), Rectangle(3, 4),
#     Square(10), Square(20)
# ]
#
# for i in geom:
#     print(i.get_per()) # одинаковое название методов. Для каждого объекта вызовется свой метод
# # 6
# # 14
# # 40
# # 80

# # у такого способа реализации также есть недостаток, например если мы создадим еще один класс и забудем прописать в нем
# # такой же метод, это приведет к ошибке
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_per(self):
#         return 4 * self.a
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     # def get_per(self): # если не создать такой метод AttributeError: 'Triangle' object has no attribute 'get_per'
#     #     return self.a + self.b + self.c
#
# geom = [
#     Rectangle(1, 2), Rectangle(3, 4),
#     Square(10), Square(20),
#     Triangle(1, 2, 3), Triangle(4, 5, 6)
# ]
#
# for i in geom:
#     print(i.get_per())

# # также есть несколько решений
# # 1 - создать базовый класс и прописать в нем этот метод, а остальные классы унаследовать от него (не лучшая реализация)
# class Figure:
#     def get_per(self):
#         return -1
#
#
# class Rectangle(Figure):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per(self):
#         return 2 * (self.w + self.h)
#
#
# class Square(Figure):
#     def __init__(self, a):
#         self.a = a
#
#     def get_per(self):
#         return 4 * self.a
#
# class Triangle(Figure):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
# geom = [
#     Rectangle(1, 2), Rectangle(3, 4),
#     Square(10), Square(20),
#     Triangle(1, 2, 3), Triangle(4, 5, 6)
# ]
#
# for i in geom:
#     print(i.get_per())
# # 6
# # 14
# # 40
# # 80
# # -1
# # -1 ошибки не возникнет, вернет результат указанный по умолчанию
#
# # лучше сделать так, чтобы у дочерних классов, была обязательная реализация данного метода
# # добавить обработку исключения, чтобы был переопределен метод
# class Figure:
#     def get_per(self): # абстракт (нет своей реализации, его нужно переопределять в дочерних классах)
#         raise NotImplementedError("В дочернем классе должен быть переопределен метод get_per")
#
#
# class Rectangle(Figure):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per(self):
#         return 2 * (self.w + self.h)
#
#
# class Square(Figure):
#     def __init__(self, a):
#         self.a = a
#
#     def get_per(self):
#         return 4 * self.a
#
# class Triangle(Figure):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
# geom = [
#     Rectangle(1, 2), Rectangle(3, 4),
#     Square(10), Square(20),
#     Triangle(1, 2, 3), Triangle(4, 5, 6)
# ]
#
# for i in geom:
#     print(i.get_per())
#
# # NotImplementedError: В дочернем классе должен быть переопределен метод get_per тогда появится исключение
#
# # методы, которые обязательно нужно переопределять, и у них нет своей реализации - называются абстрактами

# _______________  Множественное наследование  _________________
# один дочерний класс может наследоваться от нескольких базовых
# Оно не так часто используется, но все же используется, например, применение миксинов (миксины - mixins - примеси)
# в python реализуется через множественное наследование
# на примере, интернет магазина, в котором несколько различных групп товаров(свои классы, для каждой категории),
# и общий класс с полями информации по товару
# class Info:  # класс, который содержит информацию о товаре
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"Товар: {self.name}, вес: {self.weight}, цена: {self.price}")
#
#
# class Notebook(Info):  # класс для ноутбуков
#     pass
#
# note1 = Notebook("Toshiba", 1.8, 50000)
# note1.print_info()
# # Товар: Toshiba, вес: 1.8, цена: 50000

# # чтобы добавить лог (лог - например, запись о событиях в программе), логику не следует добавлять в базовый класс или по
# # иерархии создавать класс еще выше, это плохая практика. Следует создать класс миксин, который ни от какого класса не наследуется
#
# class Info:  # класс, который содержит информацию о товаре
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"Товар: {self.name}, вес: {self.weight}, цена: {self.price}")
#
#
# class Mixinlog:  # класс для логирования
#     id = 0
#
#     def __init__(self):
#         print("сработал инициализатор Mixinlog")
#         Mixinlog.id += 1
#         self.id = Mixinlog.id
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан")
#
#
# class Notebook(Info, Mixinlog):  # класс для ноутбуков + добавляем миксин с id товара
#     pass
#
# note1 = Notebook("Toshiba", 1.8, 50000)
# note1.print_info()
# note1.save_sell_log()
# # Товар: Toshiba, вес: 1.8, цена: 50000
# # 0: товар был продан

# # но __init__ класса Mixinlog не отработал, так как сначала поиск __init__ начинается в дочернем классе, если его там нет,
# # то поиск ведется уже в базовом классе (info), там он срабатывает, и поиск дальше не ведется, чтобы отработал второй
# # __init__ (класса Mixinlog) необходимо в базовом классе, прописать вызов __init__ через функцию super()
#
# class Info:  # класс, который содержит информацию о товаре
#     def __init__(self, name, weight, price):
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"Товар: {self.name}, вес: {self.weight}, цена: {self.price}")
#
#
# class Mixinlog:  # класс для логирования
#     id = 0
#
#     def __init__(self):
#         print("сработал инициализатор Mixinlog")
#         Mixinlog.id += 1
#         self.id = Mixinlog.id
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан")
#
#
# class Notebook(Info, Mixinlog):  # класс для ноутбуков + добавляем миксин с id товара
#     pass
#
# note1 = Notebook("Toshiba", 1.8, 50000)
# note1.print_info()
# note1.save_sell_log()
# # сработал инициализатор Mixinlog
# # Товар: Toshiba, вес: 1.8, цена: 50000
# # 1: товар был продан
#
# # в множественном наследовании есть определенный алгоритм обхода базовых классов MRO(Method Resolution Order)
# # Сначала обращается к дочернему классу (Notebook), ищет там необходимый метод, затем к первому базовому классу
# # (записан первым - Info), затем ко второму базовому (записан вторым - Mixinlog), и только после этого к классу object
# # именно поэтому super().__init__() срабатывает для класса Mixinlog, а не для общего класса object
#
# # список классов, по которому будем обходить можно посмотреть при помощи специального метода __mro__ (для класса, а не его экземпляра)
# print(Notebook.__mro__)
# # (<class '__main__.Notebook'>, <class '__main__.Info'>, <class '__main__.Mixinlog'>, <class 'object'>) они как раз
# # указаны в том порядке, в котором по ним и будет происходить прохождение

# именно поэтому, когда мы передаем параметры "Toshiba", 1.8, 50000 они записываются в переменные name, weight, price,
# так как __init__ класса Info срабатывает первым
# порядок важен, первым записывается как правило тот класс, в котором прописываются какие-то дополнительные параметры,
# а во вспомогательных классах, только 1 параметр self, иначе возникнут сложности в работе программы

# # если в классах одинаковое имя метода, то первым будет также вызываться тот, который прописан первым
# class Info:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"Товар: {self.name}, вес: {self.weight}, цена: {self.price}")
#
#
# class Mixinlog:  # класс для логирования
#     id = 0
#
#     def __init__(self):
#         print("сработал инициализатор Mixinlog")
#         Mixinlog.id += 1
#         self.id = Mixinlog.id
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан")
#
#     def print_info(self):
#         print("Вызов метода print_info из класса Mixinlog")
#
#
# class Notebook(Info, Mixinlog):
#     pass
#
# note1 = Notebook("Toshiba", 1.8, 50000)
# note1.print_info() # отработает метод print_info() из класса Info, так как он указан первым (Info, Mixinlog)
# # Товар: Toshiba, вес: 1.8, цена: 50000
#
# # чтобы вызвать метод другого класса, есть несколько способов
# # 1 способ - прописать сам класс, обратиться к его методу, а в качестве первого аргумента передать ссылку на экземпляр класса
# Mixinlog.print_info(note1) # Вызов метода print_info из класса Mixinlog
# # используется для единичного случая

# # 2 способ - переопределить этот метод в дочернем классе - используется, если необходимо множество раз вызывать именно
# # этот метод
# class Info:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"Товар: {self.name}, вес: {self.weight}, цена: {self.price}")
#
#
# class Mixinlog:  # класс для логирования
#     id = 0
#
#     def __init__(self):
#         print("сработал инициализатор Mixinlog")
#         Mixinlog.id += 1
#         self.id = Mixinlog.id
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан")
#
#     def print_info(self):
#         print("Вызов метода print_info из класса Mixinlog")
#
#
# class Notebook(Info, Mixinlog):
#     def print_info(self):  # так как в первую очередь метод срабатывает в дочернем классе
#         Mixinlog.print_info(self)
#
# note1 = Notebook("Toshiba", 1.8, 50000)
# note1.print_info() # Вызов метода print_info из класса Mixinlog


# # ______________  коллекция __slots__  ______________
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# # в таком виде можно свободно оперировать этими данными
# pt = Point(1, 2)
# print(pt.__dict__)  # {'x': 1, 'y': 2}
# print(pt.x)  # 1
# pt.y = 10
# # и даже задавать новые свойства
# pt.z = 3
# print(pt.__dict__)  # {'x': 1, 'y': 10, 'z': 3}

# # для того, чтобы ограничить работу с определенными данными, используются коллекция __slots__
# class Point:
#     __slots__ = ("x", "y") # указываем какие локальные переменные разрешены
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# # Мы также можем просмотреть значение и изменить его
# print(pt.x)  # 1
# pt.y = 10
# # # но задавать новые свойства не даст - выскочит ошибка
# # pt.z = 3
# # # AttributeError: 'Point' object has no attribute 'z' and no __dict__ for setting new attributes
#
# # # поскольку мы добавили в класс коллекцию __slots__, коллекция __dict__ не формируется, так что ее вызов также приведет к ошибке
# # print(pt.__dict__)
# # # AttributeError: 'Point' object has no attribute '__dict__'. Did you mean: '__dir__'?

# при этом в самом классе можно задавать любые атрибуты, ограничения лишь на локальные свойства
# class Point:
#     __slots__ = ("x", "y") # указываем какие локальные переменные разрешены
#     max_coords = 5
#
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pt = Point(1, 2)
# print(pt.max_coords)  # 5

# __slots__ также уменьшает объем занимаемой классом. можно провереть при помощи метода __sizeof__ сколько занимает
# пространство имен экземпляра класса и сама коллекция __dict__
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pt = Point(1, 2)
# print(pt.__sizeof__() + pt.__dict__.__sizeof__()) # 296

# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pt = Point(1, 2)
# print(pt.__sizeof__())  # 32

# # Также ускоряет работу с этими переменными
# import timeit # для замера скорости работы
# class Point1:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def calc(self):
#         self.x += 1
#         del self.y
#         self.y = 10
#
#
# class Point2:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def calc(self):
#         self.x += 1
#         del self.y
#         self.y = 10
#
#
# pt1 = Point1(1, 2)
# pt2 = Point2(1, 2)
# t1 = timeit.timeit(pt1.calc)
# t2 = timeit.timeit(pt2.calc)
# print(t1, t2, sep=" | ")
# # 0.29410385899973335 | 0.2597696769998947 # из-за того, что у меня комп томоз разница небольшая

# # _____________________  как работает __slots__ с property  ______________________________
# class Point:
#     __slots__ = ("x", "y", "__length")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.__length = (x * x + y * y) ** 0.5
#
# pt = Point(1, 2)
# print(pt.length)  # 2.23606797749979
        
# # но если в классе передать свойство с таким же именем
# class Point:
#     __slots__ = ("x", "y", "__length")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.__length = (x * x + y * y) ** 0.5
#     @property # через декоратор property, в сеттере и гетере прописать свойство с таким же именем length
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)  # 2.23606797749979
# pt.length = 10 # при помощи сеттера можно установить новое значение
# print(pt.length)  # 10
# # несмотря на то, что разрешено свойство в коллекции __length, методы length также отработают, так как length это атрибут
# # класса, а не локальное свойство экземпляров класса
# # коллекция __slots__ ограничивает только локальные свойства экземпляров класса, а на атрибуты самого класса не накладывает
# # никаких ограничений
#
# # при наследовании коллекция __slots__ будет работать так
# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3d(Point):
#     pass
#
#
# pt3 = Point3d(10, 20)
# pt3.z = 30
# print(pt3.z) # 30 все отработало, то есть класс Point3d не наследует коллекцию __slots__
# # причем есть даже коллекция __dict__
# print(pt3.__dict__)  # {'z': 30} свойства x и y есть, но не попадают в коллекцию __dict__
# print(pt3.x)  # 10

# # если определить в классе __slots__ даже пустую, то классу будут доступны только свойства x и y
# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3d(Point):
#     __slots__ = ()
#
#
# pt3 = Point3d(10, 20)
# pt3.z = 30 # AttributeError: 'Point3d' object has no attribute 'z' and no __dict__ for setting new attributes
# print(pt3.z)
# # попытка добавить новое свойство приведет к ошибке, но свойства x и y наследуются от базового класса

# # Если необходимо добавить свойства их нужно прописать в коллекции __slots__
# class Point:
#     __slots__ = ("x", "y")
#
#
#
# class Point3d(Point):
#     __slots__ = "z", # запятая здесь обязательна, так как коллекции __slots__ кортеж
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
# pt3 = Point3d(10, 20, 10)
# pt3.z = 30
# print(pt3.z)  # 30 все отработает без ошибок, так как мы разрешили свойство z

# # ________________________  Блоки try / except  _____________________________
# # у исключений также есть иерархия
# #               exception (класс исключений)
# #   |               |                       |               |               |
# #   V               V                       V               V               V
# # AttributeError ArithmeticError        TypeError       ValueError         ...
# # -...           - ZeroDivisionError    -...            -...
# # -...           - FloatingPointError   -...            -...
# # -...           - OverflowError        -...            -...
#
# n, m = map(int, input().split()) # 1 0
# try:  # попробовать выполнить блок кода
#     res = n / m
#     print(res)
# except ZeroDivisionError:  # Выполнить этот блок кода в случае ошибки
#     print("Делить на ноль нельзя")
# print("Программа продолжила работу, так как исключение обработано")
# # Делить на ноль нельзя
# # Программа продолжила работу, так как исключение обработано
# # отработал блок except, поэтому программа продолжила работу, несмотря на ошибку

# # зная иерархию, можно указывать общий тип для обработки ошибки, например, ArithmeticError, тогда блок except отработает
# # не только ZeroDivisionError, но и другие относящиеся к этому типу ошибки ZeroDivisionError, OverflowError и т.д.
# n, m = map(int, input().split()) # 1 0
# try:  # попробовать выполнить блок кода
#     res = n / m
#     print(res)
# except ArithmeticError:  # Выполнить этот блок кода в случае ошибки
#     print("Делить на ноль нельзя")
# print("Программа продолжила работу, так как исключение обработано")
# # Делить на ноль нельзя
# # Программа продолжила работу, так как исключение обработано

# # а exception будет отлавливать все типы ошибок
# try:
#     n, m = map(int, input().split())  # a b
#     res = n / m
#     print(res)
# except Exception:  # Этот блок отлавливает большинство ошибок, поэтому его следует указывать в конце
#     print("Некорректные данные")
# print("Программа продолжила работу, так как исключение обработано")
# # Некорректные данные
# # Программа продолжила работу, так как исключение обработано

# # Чтобы отлавливались все исключения, пишется просто except
# try:
#     n, m = map(int, input().split())  # a b
#     res = n / m
#     print(res)
# except:  # Этот блок отлавливает абсолютно все ошибки, поэтому его следует указывать в конце
#     print("Некорректные данные")
# print("Программа продолжила работу, так как исключение обработано")
# # Некорректные данные
# # Программа продолжила работу, так как исключение обработано

# ________________  блоки finally и else  ______________
#
# try:
#     n, m = map(int, input().split())  # a b
#     res = n / m
#     print(res)
# except ZeroDivisionError as z:  # также исключения можно представить в виде переменной, и затем вывести ее
#     print(z)  # division by zero (если передали 1 0)
# except ValueError as z:
#     print(z) # invalid literal for int() with base 10: 'a' (если передали a b)
# # выведется стандартное сообщение класса исключения

# # else выполняет код при штатном завершении блока try(т.е., когда программа отработает без ошибок)
# try:
#     n, m = map(int, input().split())  # 1 2
#     res = n / m
#     print(res)
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as z:
#     print(z)
# else:
#     print("Программа отработала без ошибок")
# # 0.5
# # Программа отработала без ошибок

# # если ошибка произойдет, то код в блоке else не будет выполняться
# try:
#     n, m = map(int, input().split())  # a b
#     res = n / m
#     print(res)
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as z:
#     print(z)
# else:
#     print("Программа отработала без ошибок")
# # invalid literal for int() with base 10: 'a'

# # блок finally выполняется всегда, не зависимо от исключений
# try:
#     n, m = map(int, input().split())  # a b
#     res = n / m
#     print(res)
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as z:
#     print(z)
# finally:
#     print("Это сообщение выведется в любом случае")
# # если вводятся 1 2
# # 0.5
# # Это сообщение выведется в любом случае
#
# # если вводятся a b
# # invalid literal for int() with base 10: 'a'
# # Это сообщение выведется в любом случае

# # блок используется, например при чтении и записи в файл, чтобы закрыть его, не зависимо от того была ли ошибка или нет
# try:
#     f = open("my_file.txt")
#     f.write("hello") # файл был открыт только для чтения, поэтому это приведет к ошибке
# except FileNotFoundError as er:
#     print(er)
# except:
#     print("Другая ошибка")
# finally:
#     if f:  # если файл открыт
#         f.close()
#         print("Файл был закрыт")

# # либо можно прописать менеджер контекста with он автоматически закрывает файл
# try:
#     with open("my_file.txt") as f:
#         f.write("hello") # файл был открыт только для чтения, поэтому это приведет к ошибке
# except FileNotFoundError as er:
#     print(er)
# except:
#     print("Другая ошибка")

# # есть особенность работы finally в функциях, он работает до операции return
# def get_values():
#     try:
#         x, y = map(int, input().split())
#         return x, y
#     except ValueError as er:
#         print(er)
#         return 0, 0
#     finally:
#         print("блок finally выполняется до return")
#
# n, m = get_values()
# print(n, m)
#
# # # если ввести значения 1 2
# # блок finally выполняется до return
# # 1 2
#
# # если ввести значения a b
# # invalid literal for int() with base 10: 'a'
# # блок finally выполняется до return
# # 0 0
#
# # т.е. отрабатывает блок (try или except), затем блок finally и только после оператор return
#
# # также можно прописывать вложенные блоки try except
# try:
#     x, y = map(int, input().split())
#     try:
#         div = x / y
#         print(div)
#     except ZeroDivisionError as er:
#         print(er)
# except ValueError as er:
#     print(er)
# # # если ввести значения a b
# # invalid literal for int() with base 10: 'a'
#
# # # если ввести значения 1 0
# # division by zero
#
# # # если ввести значения 1 2
# # 0.5

# # этот вложенный блок также можно вынести в отдельную функцию
# def div(a, b):
#     try:
#         return x / y
#
#     except ZeroDivisionError:
#         return "Деление на ноль"
#
# res = 0
# try:
#     x, y = map(int, input().split())  # 1 2
#     res = div(x,y)
# except ValueError as er:
#     print(er)
# print(res) # 0.5

# # _____________  распространение исключений  _____________
# # когда исключение возникает в функции, в консоли указывается строка, в которой написан код этой функции, и сторка, где
# # эта функция вызывается
# def func2():
#     res = 1 / 0
#
# print("*")
# print("**")
# print("***")
# func2()
# print("***")
# print("**")
# print("*")
# # Traceback (most recent call last):
# # *
# # **
# # ***
# #   File "E:\my_project\python_lessons\practic_oop.py", line 3904, in <module>
# #     func2()
# #     ~~~~~^^
# #   File "E:\my_project\python_lessons\practic_oop.py", line 3899, in func2
# #     res = 1 / 0
# #           ~~^~~
# # ZeroDivisionError: division by zero

# # если в другой функции вызвать функцию с ошибкой, то эта строка также будет указан
# def func2():
#     res = 1 / 0
#
# def func1():
#     func2()
#
# print("*")
# print("**")
# print("***")
# func1()
# print("***")
# print("**")
# print("*")
# #*
# # **
# # ***
# # Traceback (most recent call last):
# #   File "E:\my_project\python_lessons\practic_oop.py", line 3930, in <module>
# #     func1()
# #     ~~~~~^^
# #   File "E:\my_project\python_lessons\practic_oop.py", line 3925, in func1
# #     func2()
# #     ~~~~~^^
# #   File "E:\my_project\python_lessons\practic_oop.py", line 3922, in func2
# #     res = 1 / 0
# #           ~~^~~
# # ZeroDivisionError: division by zero

# Обработку исключения можно сделать на любом уровне стека func2 -> func1 -> main(на уровне всей программы)

# # на уровне программы
# def func2():
#     res = 1 / 0
#
# def func1():
#     func2()
#
# print("*")
# print("**")
# print("***")
# try:
#     func1()
# except:
#     print("Произошла ошибка при работе с функцией")
# print("***")
# print("**")
# print("*")
# # *
# # **
# # ***
# # Произошла ошибка при работе с функцией
# # ***
# # **
# # *

# # на уровне первой функции - также все отработает
# def func2():
#     res = 1 / 0
#
# def func1():
#     try:
#         return func2()
#     except:
#         print("Произошла ошибка при работе с функцией")
#
# print("*")
# print("**")
# print("***")
# func1()
# print("***")
# print("**")
# print("*")
# # *
# # **
# # ***
# # Произошла ошибка при работе с функцией
# # ***
# # **
# # *

# # при этом, если обработать ошибку на более раннем стеке, она дальше обрабатываться не будет, так как уже обработана
# def func2():
#     try:
#         return 1 / 0
#     except:
#         print("Ошибка в функции func2")
#
# def func1():
#     try:
#         return func2()
#     except:
#         print("Произошла ошибка при работе с функцией")
#
# print("*")
# print("**")
# print("***")
# func1()
# print("***")
# print("**")
# print("*")
# # *
# # **
# # ***
# # Ошибка в функции func2
# # ***
# # **
# # *

# ______________  инструкция raise и пользовательские исключения  _____________
# # При помощи raise можно сгенерировать исключение
# print("*")
# print("**")
# print("***")
# raise ZeroDivisionError # сработает исключение, хотя деления на ноль в программе нет
# print("***")
# print("**")
# print("*")
# # Traceback (most recent call last):
# #   File "E:\my_project\python_lessons\practic_oop.py", line 4034, in <module>
# #     raise ZeroDivisionError
# # ZeroDivisionError
# # *
# # **
# # ***

# # можно указать свое сообщение ошибки
# print("*")
# print("**")
# print("***")
# raise ZeroDivisionError("Ошибка - на ноль делить нельзя")
# print("***")
# print("**")
# print("*")
# # *
# # **
# # ***
# # Traceback (most recent call last):
# #   File "E:\my_project\python_lessons\practic_oop.py", line 4050, in <module>
# #     raise ZeroDivisionError("Ошибка - на ноль делить нельзя")
# # ZeroDivisionError: Ошибка - на ноль делить нельзя

# # можно присвоить переменной экземпляр класса исключения, а затем указать ее в операторе raise
# print("*")
# print("**")
# print("***")
# er = ZeroDivisionError("Ошибка - на ноль делить нельзя")
# raise er
# print("***")
# print("**")
# print("*")
# # *
# # **
# # ***
# # Traceback (most recent call last):
# #   File "E:\my_project\python_lessons\practic_oop.py", line 4067, in <module>
# #     raise er
# # ZeroDivisionError: Ошибка - на ноль делить нельзя

# # используется, когда стандартных классов исключений недостаточно
# # Например, при ошибке при работе принтера
# class PrintData:
#     def print_data(self, data):
#         self.send_data(data)
#         print(f'Печать: {str(data)}')
#
#     def send_data(self, data):
#         if not self.send_to_print(data):
#             raise Exception("Принтер не отвечает")
#
#     def send_to_print(self, data):
#         return False  # имитация ошибки подключения
#
# p = PrintData()
# p.print_data("Какой-то документ на печать")
# # Traceback (most recent call last):
# #   File "E:\my_project\python_lessons\practic_oop.py", line 4094, in <module>
# #     p.print_data("Какой-то документ на печать")
# #     ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# #   File "E:\my_project\python_lessons\practic_oop.py", line 4083, in print_data
# #     self.send_data(data)
# #     ~~~~~~~~~~~~~~^^^^^^
# #   File "E:\my_project\python_lessons\practic_oop.py", line 4088, in send_data
# #     raise Exception("Принтер не отвечает")
# # Exception: Принтер не отвечает

# # Это исключение можно также обработать, чтобы программа не прерывалась с ошибкой
# class PrintData:
#     def print_data(self, data):
#         self.send_data(data)
#         print(f'Печать: {str(data)}')
#
#     def send_data(self, data):
#         if not self.send_to_print(data):
#             raise Exception("Принтер не отвечает")
#
#     def send_to_print(self, data):
#         return False
#
# p = PrintData()
# try:
#     p.print_data("Какой-то документ на печать")
# except Exception:
#     print("Ошибка подключения принтера")
# # Ошибка подключения принтера

# # а когда данные отправляются успешно, идет печать документа
# class PrintData:
#     def print_data(self, data):
#         self.send_data(data)
#         print(f'Печать: {str(data)}')
#
#     def send_data(self, data):
#         if not self.send_to_print(data):
#             raise Exception("Принтер не отвечает")
#
#     def send_to_print(self, data):
#         return True  # ошибка подключения была исправлена
#
# p = PrintData()
# try:
#     p.print_data("Какой-то документ")
# except Exception:
#     print("Ошибка подключения принтера")
# # Печать: Какой-то документ

# # причем можно создать свой класс исключение - на основе базового класса Exception
# class SendPrintError(Exception):  # так как наследуем от Exception базовый функционал уже заложен
#     # pass # можно поставить pass
#     """Для обработки ошибки подключения принтера"""  # принято оставлять комментарий для чего этот класс
#
# class PrintData:
#     def print_data(self, data):
#         self.send_data(data)
#         print(f'Печать: {str(data)}')
#
#     def send_data(self, data):
#         if not self.send_to_print(data):
#             raise SendPrintError("Принтер не отвечает")
#
#     def send_to_print(self, data):
#         return False
#
# p = PrintData()
# try:
#     p.print_data("Какой-то документ")
# except SendPrintError:
#     print("Ошибка подключения принтера")
# # Ошибка подключения принтера

# # в своем классе исключения можно прописать свой функционал
# class SendPrintError(Exception):
#     """Для обработки ошибки подключения принтера"""
#
#     def __init__(self, *args):
#         self.message = args[0] if args else None # если есть аргументы, внести их в massage (сообщение исключения)
#
#     def __str__(self):  # переопределяем вывод сообщения
#         return f"Ошибка : {self.message}"
#
#
# class PrintData:
#     def print_data(self, data):
#         self.send_data(data)
#         print(f'Печать: {str(data)}')
#
#     def send_data(self, data):
#         if not self.send_to_print(data):
#             raise SendPrintError("Принтер не отвечает")
#
#     def send_to_print(self, data):
#         return False
#
# p = PrintData()
# p.print_data("Какой-то документ")
# # try:
# #     p.print_data("Какой-то документ")
# # except SendPrintError:
# #     print("Ошибка подключения принтера")
# # Traceback (most recent call last):
# #   File "E:\my_project\python_lessons\practic_oop.py", line 4194, in <module>
# #     p.print_data("Какой-то документ")
# #     ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
# #   File "E:\my_project\python_lessons\practic_oop.py", line 4183, in print_data
# #     self.send_data(data)
# #     ~~~~~~~~~~~~~~^^^^^^
# #   File "E:\my_project\python_lessons\practic_oop.py", line 4188, in send_data
# #     raise SendPrintError("Принтер не отвечает")
# # SendPrintError: Ошибка : Принтер не отвечает

# # также можно прописать свою иерархию исключений
# class PrintError(Exception):
#
#     def __str__(self):  # переопределяем вывод сообщения
#         """Общий класс исключений работы принтера"""
#
#
# class SendPrintError(PrintError):
#     """Для обработки ошибки подключения принтера"""
#
#     def __init__(self, *args):
#         self.message = args[0] if args else None # если есть аргументы, внести их в massage (сообщение исключения)
#
#     def __str__(self):  # переопределяем вывод сообщения
#         return f"Ошибка при передаче данных: {self.message}"
#
#
# class PrintData:
#     def print_data(self, data):
#         self.send_data(data)
#         print(f'Печать: {str(data)}')
#
#     def send_data(self, data):
#         if not self.send_to_print(data):
#             raise SendPrintError("Принтер не отвечает")
#
#     def send_to_print(self, data):
#         return False
#
# p = PrintData()
# try:
#     p.print_data("Какой-то документ")
# except SendPrintError:
#     print("ошибка: нет ответа от принтера")
# except PrintError:
#     print("Другая ошибка в работе принтера")

# # ______________________________  менеджер контекста with  _____________________________________
# # на примере открытия файла
# # при открытии файла, его необходимо закрыть, независимо от того, произошла ли ошибка, поэтому функция close()
# # помещается в блок finally
# fp = None
# try:
#     fp = open("file.txt")
#     for i in fp:
#         print(i)
# except Exception as er:
#     print(er)
# finally:
#     if fp:
#         fp.close()
#
# # Если при помощи менеджера контекста открывать, то закрывать файл не нужно, так как он закрывает его автоматически
# fp = None
# try:
#     with open("file.txt") as fp:
#         for i in fp:
#             print(i)
# except Exception as er:
#     print(er)

# менеджер контекста - это класс, в котором реализовано 2 магических метода:
# __enter__() - срабатывает в момент создания объекта менеджера контекста
# __exit__() - срабатывает в момент завершения работы менеджера контекста или возникновения исключения

# # пример cоздания своего менеджера контекста
# # задан вектор, мы вносим в него изменения, но в случае возникновения каких-либо ошибок, эти изменения
# # не должны быть внесены
# class DefenedVector:
#     def __init__(self, v):
#         self.__v = v  # приватное локальное свойство, в котором сохраним вектор
#
#     # поскольку этот класс у нас менеджер контекста, нужно определить два магических метода
#     def __enter__(self):
#         self.__temp = self.__v[:] # создадим еще одно приватное свойства, которое будет ссылаться на копию начального вектора
#         return self.__temp  # на эту копию и будет ссылаться переменная dv
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:  # Если не произошло никаких ошибок exc_type = None
#             self.__v[:] = self.__temp  # self.__v[:] = self.__temp этот синтаксис означает , что вв список V поэлементно копируется список temp
#             return self.__v
#
#         return False #  в блоке кода менеджера контекста исключения обрабатываться не будут
#     # если бы было True, то они обрабатывались бы внутри менеджера контекста
#
#
#
# v1 = [1, 2, 3]  # начальный вектор
# v2 = [4, 5]  # тот, на который будем менять начальный вектор
#
# with DefenedVector(v1) as dv:  # в класс передаем тот вектор, который хотим защитить от ошибки
#     for i, a in enumerate(dv):
#         dv[i] += v2[i]  # так как размер v1 > v2 здесь возникнет ошибка
#
# print(v1)
# # возникнет такая ошибка, чтобы убедиться, что вектор V1 не изменится, поместим в конструкцию try - except
# # Traceback (most recent call last):
# #   File "E:\my_project\python_lessons\practic_oop.py", line 4302, in <module>
# #     dv[i] += v2[i]  # так как размер v1 > v2 здесь возникнет ошибка
# #              ~~^^^
# # IndexError: list index out of range
#
# class DefenedVector:
#     def __init__(self, v):
#         self.__v = v
#
#
#     def __enter__(self):
#         self.__temp = self.__v[:]
#         return self.__temp
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.__v[:] = self.__temp
#             return self.__v
#
#         return False #
#
#
# v1 = [1, 2, 3]
# v2 = [4, 5]
# try:
#     with DefenedVector(v1) as dv:
#         for i, a in enumerate(dv):
#             dv[i] += v2[i]
# except:
#     print("Возникла ошибка")
# print(v1)
# # Возникла ошибка
# # [1, 2, 3] # значение вектора не изменилось, так как возникло исключение, но если размер списков будет одинаковый,
# # вектор изменится

# class DefenedVector:
#     def __init__(self, v):
#         self.__v = v
#
#
#     def __enter__(self):
#         self.__temp = self.__v[:]
#         return self.__temp
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.__v[:] = self.__temp
#             return self.__v
#
#         return False #
#
#
# v1 = [1, 2, 3]
# v2 = [4, 5, 6]
# try:
#     with DefenedVector(v1) as dv:
#         for i, a in enumerate(dv):
#             dv[i] += v2[i]
# except:
#     print("Возникла ошибка")
# print(v1)
# # [5, 7, 9] # вектор изменился

# # без менеджера контекста даже с ошибкой вектор был бы изменен
# v1 = [1, 2, 3]
# v2 = [4, 5]
# try:
#     for i, a in enumerate(v1):
#         v1[i] += v2[i]
# except:
#     print("Возникла ошибка")
# print(v1)
# # Возникла ошибка
# # [5, 7, 3] # вектор изменился, несмотря на возникшую ошибку

# ___________