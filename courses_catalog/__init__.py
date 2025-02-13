# name = "Каталог с курсами по программированию"

# import courses_catalog.python_lessons
# import courses_catalog.css
# import courses_catalog.html
# import courses_catalog.java
#
# name = "Каталог с курсами по программированию"

# from courses_catalog.python_lessons import func_python
# from courses_catalog.css import func_css
# from courses_catalog.html import func_html
# from courses_catalog.java import func_java
#
# name = "Каталог с курсами по программированию"

# from courses_catalog.python_lessons import func_python это абсолютный импорт, если изменится имя каталога, придется его менять
# во всех импортах. Поэтому удобнее использовать относительный импорт (через точку - . обращение к текущему каталогу)
# from .python_lessons import func_python
# from .css import func_css
# from .html import func_html
# from .java import func_java

# для импорта модулей (когда нужно будет прописывать имя файла также можно прописать через точку
# from . import python_lessons # обращение к текущему каталогу

# # для импорта каталога приемлемо использовать *, так как файлы дорабатываются, а функции добавляются
# from .python_lessons import *

from .doc import *
