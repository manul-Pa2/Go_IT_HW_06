import sys
from pathlib import Path

from colorama import init, Fore, Style


init(autoreset=True)       # Активує колораму


def print_tree(path: Path, prefix: str = "") -> None:
    try:                                             # Список елементів папки (спочатку папки, потім файли) + перевірка помилки
        items = list(path.iterdir())
    except OSError as e:
        print(prefix + Fore.RED + f"[Помилка доступу: {e}]")
        return

    items.sort(key=lambda p: (p.is_file(), p.name.lower()))

    for index, item in enumerate(items):
        connector = "└── " if index == len(items) - 1 else "├── "

        if item.is_dir():
            print(prefix + connector + Fore.BLUE + Style.BRIGHT + item.name)   # Підсвічує директорії – синім кольором
            
            extension_prefix = "    " if index == len(items) - 1 else "│   "
            print_tree(item, prefix + extension_prefix)
        else:
            print(prefix + connector + Fore.GREEN + item.name)        # Підсвічуємо текст зеленим (як у прикладі з лекції)


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "Використання:\n"
            "  python hw03.py /шлях/до/директорії"
        )
        return 1

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + f"Помилка: Шлях '{dir_path}' не існує.")
        return 1

    if not dir_path.is_dir():
        print(Fore.RED + f"Помилка: '{dir_path}' не є директорією.")
        return 1
      
    print(Fore.MAGENTA + Style.BRIGHT + dir_path.name)     #Коренева директорія
    print_tree(dir_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

 # Тут повинен бути шлях до директорії, але я не певен як його правильно задати, в інтернеті кажуть що це робиться командами Bash, які ми ще не проходили(((
