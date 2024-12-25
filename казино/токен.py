import abc as абц
import builtins as встроенные
import functools as функинстр
from dataclasses import dataclass as _классданных

from константы import КОДЫ_ДВОИЧН_ОП as КОД_ДВОП
from операции import питон
from операции.база import Оп
from структуры import ПромежутТаблицаИмен, ТаблицаКонст
from типы import Список, Мб, Ничего, СтдТипы

классданных = функинстр.partial(_классданных, frozen=True, slots=True)()

class Токен(абц.ABC):

    def генерир_опы(сам, табл_им: ПромежутТаблицаИмен, табл_конст: ТаблицаКонст) -> Список[Оп]: 
        ...

class ТипДанных(Токен):
    значение: СтдТипы
    __match_args__ = ("значение",)

    def генерир_опы(сам, табл_им: ПромежутТаблицаИмен, табл_конст: ТаблицаКонст) -> Список[Оп]:
        __import__('ipdb').set_trace()
        конст_ид = табл_конст.найти_или_создать(сам.значение)
        return [питон.ЗагрКонст(конст_ид)]

@классданных
class ЦелоеЧисло(ТипДанных):
    значение: int

@классданных
class ВещественноеЧисло(ТипДанных):
    значение: float

@классданных
class Строка(ТипДанных):
    значение: str

@классданных
class Булево(ТипДанных):
    значение: bool

@классданных
class Переменная(Токен):
    имя: str

@классданных
class Функция(Токен):
    имя: str

@классданных
class Вызов(Токен):
    функция: Функция
    аргументы: Список[Переменная | ТипДанных]

    def генерир_опы(сам, табл_им: ПромежутТаблицаИмен, табл_конст: ТаблицаКонст) -> Список[Оп]:
        опы = []
        if сам.приводимое_к_двопу():
            сам.обработать_аргументы(опы, табл_им, табл_конст)
            match сам.функция.имя:
                case "умн": опы.append(питон.ДвоичнОп(КОД_ДВОП["УМНОЖЕНИЕ"]))
                case "слж": опы.append(питон.ДвоичнОп(КОД_ДВОП["СЛОЖЕНИЕ"]))
        else:
            опы.append(питон.ТолкнутьНуль())
            if сам.функция.имя == "говорим":
                запись_фн = табл_им.найти_или_создать("print", встроенные.print)
            elif сам.функция.имя == "как_вы_хотите":
                запись_фн = табл_им.найти_или_создать("input", встроенные.input)
            elif сам.функция.имя == "Целое":
                запись_фн = табл_им.найти_или_создать("int", int)
            else:
                raise NotImplementedError(сам.функция.имя)
            опы.append(питон.ЗагрИмя(запись_фн.ид))
            сам.обработать_аргументы(опы, табл_им, табл_конст)
            опы.append(питон.Вызвать(len(сам.аргументы)))
        return опы

    def приводимое_к_двопу(сам) -> bool:
        return сам.функция.имя in {"слж", "умн"}

    def обработать_аргументы(
        сам, опы: Список[Оп], табл_им: ПромежутТаблицаИмен, табл_конст: ТаблицаКонст
    ):
        for арг in сам.аргументы:
            match арг:
                case Переменная(имя):
                    ид_имя = табл_им[имя].ид
                    опы.append(питон.ЗагрИмя(ид_имя))
                case ТипДанных(знач):
                    ид_конст = табл_конст.найти_или_создать(знач)
                    опы.append(питон.ЗагрКонст(ид_конст))
                case вызов if isinstance(вызов, Вызов):
                    опы.extend(вызов.генерир_опы(табл_им, табл_конст))


@классданных
class ОбъявлениеПеременной(Токен):
    имя: str
    значение: Мб[Вызов | ТипДанных]

    def генерир_опы(сам, табл_им: ПромежутТаблицаИмен, табл_конст: ТаблицаКонст) -> Список[Оп]:
        опы = []
        if isinstance(сам.значение, Вызов):
            опы.extend(сам.значение.генерир_опы(табл_им, табл_конст))
        elif сам.значение is Ничего or isinstance(сам.значение, ТипДанных):
            конст_ид = табл_конст.найти_или_создать(сам.значение)
            опы.append(питон.ЗагрКонст(конст_ид))
        имя_ид = табл_им.найти_или_создать(сам.имя, сам.значение).ид
        опы.append(питон.СохрКакИмя(имя_ид))
        return опы

@классданных
class Присвоение(Токен):
    имя: str
    # значение: str
    значение: Мб[Вызов | ТипДанных]

    def генерир_опы(сам, табл_им: ПромежутТаблицаИмен, табл_конст: ТаблицаКонст) -> Список[Оп]:
        опы = []
        if isinstance(сам.значение, Вызов):
            опы.extend(сам.значение.генерир_опы(табл_им, табл_конст))
        elif сам.значение is Ничего or isinstance(сам.значение, ТипДанных):
            конст_ид = табл_конст.найти_или_создать(сам.значение)
            опы.append(питон.ЗагрКонст(конст_ид))
        имя_ид = табл_им.найти_или_создать(сам.имя, сам.значение).ид
        опы.append(питон.СохрКакИмя(имя_ид))
        return опы

