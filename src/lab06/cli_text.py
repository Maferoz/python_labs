import argparse
import pathlib
from src.lib.text import normalize, tokenize, count_freq, top_n
import sys

def main() -> None:
    parser = argparse.ArgumentParser(description= "Текстовые утилиты")
    subparsers = parser.add_subparsers(dest = "command", required = True)

    cat_parser = subparsers.add_parser("cat", help = "Вывод содержимого файла построчно")
    cat_parser.add_argument("--input", required = True, help = "Путь к файлу")
    cat_parser.add_argument("-n", action = "store_true", help = "Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help = "Анализ частоты слов в тексте")
    stats_parser.add_argument("--input", required = True, help = "Путь к текстовому файлу")
    stats_parser.add_argument("--top", type = int, default = 5, help = "Кол-во топ-слов")

    args = parser.parse_args()

# Обработка команды cat
    if args.command == "cat":
        file_path = pathlib.Path(args.input)
        if not file_path.exists():
            print(f"Файл {file_path} не найден", file = sys.stderr)
            return
        with open(file_path, "r", encoding = "utf-8") as f:
            for idx, line in enumerate(f,start = 1):
                if args.n:
                    print(f"{idx:4} | {line}", end = "")
                else:
                    print(line, end = "")

# Обработка команды stats
    elif args.command == "stats":
        file_path = pathlib.Path(args.input)
        if not file_path.exists():
            print(f"Файл {file_path} не найден", file = sys.stderr)
            return
        with open(file_path, "r", encoding = "UTF-8") as f:
            content = f.read()
            tokens = tokenize(normalize(content))
            freq = count_freq(tokens)
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq)}")
        print(f"Топ-{args.top}:")
        for word, count in top_n(freq, n=args.top):
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()

# python3 -m src.lab06.cli_text cat --input data/samples/people.csv -n
# python3 -m src.lab06.cli_text stats --input data/samples/text.txt --top 5