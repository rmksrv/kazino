from functools import partial as частичн
from dataclasses import dataclass as _классданных

from типы import СтдТипы, ТаблицаИмен, КонстПул
from утилиты import йота

классданных = частичн(_классданных, frozen=True, slots=True)()


@классданных
class ДанныеИмени:
    ид: int
    знач: СтдТипы


class ПромежутТаблицаИмен(dict):

    def __init__(сам, *арги, **ксарги):
        super(ПромежутТаблицаИмен, сам).__init__(*арги, **ксарги)
        сам.ид = str(id(сам))

    def найти_или_создать(сам, имя: str, знач: "СтдТипы | ТипДанных") -> ДанныеИмени:
        try:
            знач = знач.значение
        except AttributeError:
            pass
        if имя not in сам:
            сам[имя] = ДанныеИмени(йота(сам.ид), знач)
        return сам[имя]

    def как_стд_таблица_имен(сам) -> ТаблицаИмен:
        return {
            данные.ид: (имя, данные.знач)
            for имя, данные in сам.items()
        }



class ТаблицаКонст(dict):

    def __init__(сам, *арги, **ксарги):
        super(ТаблицаКонст, сам).__init__(*арги, **ксарги)
        сам.ид = str(id(сам))

    def найти_или_создать(сам, знач: "СтдТипы | ТипДанных") -> int:
        try:
            знач = знач.значение
        except AttributeError:
            pass
        if знач not in сам:
            сам[знач] = йота(сам.ид)
        return сам[знач]

    def как_констпул(сам) -> КонстПул:
        return tuple(знач for знач in sorted(сам, key=сам.get))

