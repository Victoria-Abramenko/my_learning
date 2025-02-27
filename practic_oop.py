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




