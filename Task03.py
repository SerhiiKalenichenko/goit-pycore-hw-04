from pathlib import Path
import sys
from colorama import init, Fore, Style

init(autoreset=True)

DIR_COLOR = Fore.CYAN + Style.BRIGHT
FILE_COLOR = Fore.WHITE

def tree(path: Path, prefix: str = "", is_last: bool = True) -> None:
    entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    connectors = {"mid": "├── ", "last": "└── ", "pipe": "│   ", "space": "    "}

    for idx, entry in enumerate(entries):
        last = idx == len(entries) - 1
        connector = connectors["last"] if last else connectors["mid"]
        next_prefix = prefix + (connectors["space"] if last else connectors["pipe"])

        if entry.is_dir():
            print(prefix + connector + DIR_COLOR + entry.name + Style.RESET_ALL)
            try:
                tree(entry, next_prefix, last)  # рекурсивний обхід
            except PermissionError:
                print(next_prefix + FILE_COLOR + "[Немає доступу]" + Style.RESET_ALL)
        else:
            print(prefix + connector + FILE_COLOR + entry.name + Style.RESET_ALL)


def main():
    if len(sys.argv) < 2:
        print("Використання: python hw03.py <шлях_до_директорії>")
        sys.exit(1)

    root = Path(sys.argv[1]).expanduser().resolve()

    if not root.exists():
        print("Помилка: вказаний шлях не існує.")
        sys.exit(2)
    if not root.is_dir():
        print("Помилка: шлях має вказувати на директорію.")
        sys.exit(3)

    print(DIR_COLOR + root.name + Style.RESET_ALL)
    tree(root)

if __name__ == "__main__":
    main()
