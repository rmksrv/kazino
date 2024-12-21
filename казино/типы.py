import typing as т

type ПроизвКортеж[Т] = tuple[Т, ...]
type Список[T] = list[T]
type Словарь[K, V] = dict[K, V]
type СтдТипы = str | int | float | bool | None
type Вызывабельное = т.Callable
type Стэк = Список[СтдТипы | Вызывабельное]
type ТаблицаИмен = Словарь[int, tuple[str, СтдТипы | Вызывабельное]]
type КонстПул = ПроизвКортеж[СтдТипы]

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

