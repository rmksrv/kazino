import abc as абц
from typing import Self as Сам

from казино.интер import Интерпретатор
from казино.типы import Ничего

class Оп(абц.ABC):
    __аргументы__ = tuple()

    @абц.abstractmethod
    def исполнить(сам, интер: Интерпретатор): ...

    @абц.abstractmethod
    def компилировать(сам) -> bytes: ...

    def __repr__(сам) -> str:
        return f"{сам.__class__.__name__}{vars(сам)}"

    def __len__(сам) -> int:
        return len(сам.__аргументы__) + 1

    def сдвинуть_текущий_индекс_оп(сам, интер: Интерпретатор, *, сдвиг: int | Ничего = Ничего):
        сдвиг = сдвиг or len(сам)
        интер.тек_инд_оп += сдвиг

    def кортеж_с_аргументами(сам) -> tuple[Сам, ...]:
        значения = [зн for имя, зн in vars(сам).items() if имя in сам.__аргументы__]
        return (сам, *значения)

