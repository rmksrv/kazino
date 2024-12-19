import typing as т

type Кортеж = tuple
type Список[T] = list[T]
type Словарь[K, V] = dict[K, V]
type Стэк = Список[int]
type СтдТипы = str | int | float | bool | None
type Вызывабельное = т.Callable
type ТаблицаИмен = Словарь[int, Кортеж[str, СтдТипы | Вызывабельное]]
type КонстПул = Кортеж[СтдТипы, ...]

Ничего = None
Мб = т.Optional

class Нуль:

    _экз = Ничего

    def __call__(сам):
        if сам._экз is Ничего:
            сам._экз = Нуль()
        return сам._экз

    def __repr__(сам) -> str:
        return "NULL"

