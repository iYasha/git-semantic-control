from colorama import Back, Fore
from typing import *


class ExceptionFormatter:
    @staticmethod
    def format(msg: str, detail: Optional[str] = ''):
        print(f'{Fore.RED}{msg}\n{Fore.RESET}{detail}')
