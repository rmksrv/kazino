import typing as т
from казино.утилиты import Одиночка

type ПроизвКортеж[Т] = tuple[Т, ...]
type Список[T] = list[T]
type Набор[T] = set[T]
type Словарь[K, V] = dict[K, V]
type СтдТипы = str | int | float | bool | None
type Вызывабельное = т.Callable

Ничего = None
Мб = т.Optional

class Нуль(metaclass=Одиночка):
    def __repr__(сам) -> str:  return "NULL"


type Стэк = Список[СтдТипы | Вызывабельное | Нуль]
type ТаблицаИмен = Словарь[int, tuple[str, СтдТипы | Вызывабельное | Нуль]]
type КонстПул = ПроизвКортеж[СтдТипы | Вызывабельное | Нуль]
