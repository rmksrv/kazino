import typing as т
from утилиты import Одиночка

type ПроизвКортеж[Т] = tuple[Т, ...]
type Список[T] = list[T]
type Набор[T] = set[T]
type Словарь[K, V] = dict[K, V]
type СтдТипы = str | int | float | bool | None
type Вызывабельное = т.Callable
type Стэк = Список[СтдТипы | Вызывабельное]
type ТаблицаИмен = Словарь[int, tuple[str, СтдТипы | Вызывабельное]]
type КонстПул = ПроизвКортеж[СтдТипы]

Ничего = None
Мб = т.Optional

class Нуль(metaclass=Одиночка):
    def __repr__(сам) -> str:  return "NULL"

