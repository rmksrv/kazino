import sys as сис
import typing as т
from collections import defaultdict as умолчслов

type Отображение[А, Б] = т.Callable[[А], Б]
type Предикат[А] = т.Callable[[А], bool]


class Одиночка(type):

    _экземпляры = {}

    def __call__(клс, *арг, **ксарг):
        if клс not in клс._экземпляры:
            клс._экземпляры[клс] = super(Одиночка, клс).__call__(*арг, **ксарг)
        return клс._экземпляры[клс]


def выйти_с_ошибкой(текст_или_искл: str | Exception, код_выхода: int = -1):
    текст = str(текст_или_искл)
    print(f"ОШИБКА: {текст}")
    сис.exit(код_выхода)


class Поток[А, Б]:

    def __init__(сам, коллекц):
        сам.коллекц = коллекц

    def прим(сам, функ: Отображение[А, т.Any]) -> т.Self:
        сам.коллекц = [функ(о) for о in сам.коллекц]
        return сам

    def фильтр(сам, функ: Предикат[А]) -> т.Self:
        сам.коллекц = [о for о in сам.коллекц if функ(о)]
        return сам

    def собрать(сам, тип: type) -> т.Iterable[Б]:
        return тип(сам.коллекц)


_йоты = умолчслов(lambda: -1)


def йота(имя: str, сброс: bool = False) -> int:
    global _йоты

    if сброс:
        _йоты[имя] = 0
    else:
        _йоты[имя] += 1
    return _йоты[имя]


def подними_исключение(e: Exception) -> None:
    raise e

