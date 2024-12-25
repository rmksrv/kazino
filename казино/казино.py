import argparse as аргпарс
import marshal as маршал
import pathlib as путьбиб
import struct as структ
import subprocess as подпроц
import time as время
import types as питипы

from казино.исключения import Искл
from казино.парсер import получить_программу
from казино.программа import Программа
from казино.константы import МАГИЧЕСКОЕ_ЧИСЛО_ПИТОНА
from казино.утилиты import выйти_с_ошибкой


def интерпретировать(программа: Программа, допвывод: bool):
    стэк = []
    for операция in программа.операции:
        if допвывод:
            print(f"Стэк:         {стэк}")
            print(f"Таблица имен: {программа.таблица_имен}")
            print(f"Операция:     {операция.__class__.__name__}{vars(операция)}")
        операция.исполнить(стэк, программа.таблица_имен, программа.конст_пул)
        if допвывод:
            print("-" * 30)
            print()


def компилировать(программа: Программа, вывод_файл: путьбиб.Path, пуск: bool):
    байткод = b"".join(оп.компилировать() for оп in программа.операции)
    код_тип = питипы.CodeType(
        0,                      # argcount
        0,                      # posonlyargcount
        0,                      # kwonlyargcount
        0,                      # nlocals
        10,                      # stacksize
        64,                     # flags
        байткод,                # codestring
        программа.конст_пул,    # consts
        программа.кортеж_имен,  # names
        (),                     # varnames
        "test.py",              # filename
        "<module>",             # name
        "<module>",             # qualname
        1,                      # firstlineno
        b"",                    # linetable
        b"",                    # exceptiontable
        # optional
        (),                     # freevars
        (),                     # cellvars
    )
    времштамп = int(время.time())
    разм_файла = 0

    with вывод_файл.open("wb") as ф:
        ф.write(МАГИЧЕСКОЕ_ЧИСЛО_ПИТОНА)
        ф.write(структ.pack("I", времштамп))
        ф.write(структ.pack("I", разм_файла))
        ф.write(маршал.dumps(код_тип))

    if пуск:
        подпроц.call(["python", вывод_файл])


def парсить_аргументы() -> аргпарс.Namespace:
    парсер = аргпарс.ArgumentParser(prog="казино")
    субпарсеры = парсер.add_subparsers(dest="команда")

    парсер_комп = субпарсеры.add_parser("комп")
    парсер_комп.add_argument("--пуск", action="store_true", default=False)
    парсер_комп.add_argument("--выходной-файл", type=str, default="./out.pyc")

    парсер_интер = субпарсеры.add_parser("интер")

    парсер.add_argument("файл", type=str)
    парсер.add_argument("--допвывод", action="store_true", default=False)

    return парсер.parse_args()


def преобразовать_файл_в_программу(файл: путьбиб.Path, допвывод: bool) -> Программа:
    if not файл.exists():
        выйти_с_ошибкой(f"Файл {файл} не найден")
    try:
        return получить_программу(файл, допвывод=допвывод)
    except Искл as и:
        выйти_с_ошибкой(и)


def главная():
    аргументы = парсить_аргументы()
    файл = путьбиб.Path(аргументы.файл)
    прог = преобразовать_файл_в_программу(файл, аргументы.допвывод)
    match аргументы.команда:
        case "комп": компилировать(прог, путьбиб.Path(аргументы.выходной_файл), пуск=аргументы.пуск)
        case "интер": интерпретировать(прог, допвывод=аргументы.допвывод)
        case _: выйти_с_ошибкой(f"Неизвестная команда `{аргументы.команда}`")


if __name__ == "__main__":
    главная()

