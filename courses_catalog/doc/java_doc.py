# если необходимо обратиться к внешнему модулю(из вложенного)
from ..java import func_java # при запуске этого ImportError: attempted relative import with no known parent package


java = "Типа тут документация по java: " + func_java()

  # запуск функции из внешнего модуля