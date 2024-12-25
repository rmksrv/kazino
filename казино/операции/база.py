import abc as абц

from казино.типы import Стэк, ТаблицаИмен, КонстПул


class Оп(абц.ABC):

    @абц.abstractmethod
    def исполнить(сам, стэк: Стэк, таблица_имен: ТаблицаИмен, конст_пул: КонстПул): ...

    @абц.abstractmethod
    def компилировать(сам) -> bytes: ...

    def __repr__(сам) -> str:
        return f"{сам.__class__.__name__}{vars(сам)}"

