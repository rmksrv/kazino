import pathlib as путьбиб
import shlex as шлекс
import sys as сис
import subprocess as подпроц
from dataclasses import dataclass as датакласс
from typing import Self as Сам


КОРЕНЬ_ДИР = путьбиб.Path(__file__).parent.parent


@датакласс(frozen=True, slots=True)
class ДанныеПроцесса:
    код_возвр: int
    стд_вывод: str
    стд_ошибк: str

    @classmethod
    def из(клс, проц: подпроц.CompletedProcess) -> Сам:
        return клс(
            код_возвр=проц.returncode,
            стд_вывод=проц.stdout.decode("utf-8"),
            стд_ошибк=проц.stderr.decode("utf-8"),
        )


def исполнить(команда: str) -> ДанныеПроцесса:
    это_позикс = сис.platform != "win32"
    части_команды = шлекс.split(команда, posix=это_позикс)
    процесс = подпроц.run(части_команды, stdout=подпроц.PIPE, stderr=подпроц.PIPE)
    return ДанныеПроцесса.из(процесс)

