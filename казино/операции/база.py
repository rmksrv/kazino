from типы import Стэк, ТаблицаИмен, КонстПул


class Оп:

    def исполнить(сам, стэк: Стэк, таблица_имен: ТаблицаИмен, конст_пул: КонстПул):
        raise NotImplemented

    def компилировать(сам) -> bytes:
        raise NotImplemented

