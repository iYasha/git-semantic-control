"""
entrypoint gsc
"""
from gcv import GCV
import os
import argparse


def get_args() -> argparse.Namespace:
    """
    Парсит агрументы которые пользователь ввел при запуске программы
    :return: Namespace обьектов которые удалось спарсить
    """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-m', required=True, dest='message',
                        help='Commit message')
    parser.add_argument('-v', required=False, dest='version',
                        help='Commit version. Example: 0.1.3')
    parser.add_argument('--version', action='version',
                        version='GSC 0.1.0', help="Show program's version number and exit.")
    return parser.parse_args()


def main():
    args = get_args()
    path = os.getcwd()
    gcv = GCV(path, args.message, version=args.version)


if __name__ == '__main__':
    main()
