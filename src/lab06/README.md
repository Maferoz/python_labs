## Stats and cat
```
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
```
### Для cat:
> INPUT: python3 -m src.lab06.cli_text cat --input data/samples/people.csv -n

> OUTPUT: <img width="429" height="90" alt="image" src="https://github.com/user-attachments/assets/ec546bb7-87bd-4e92-b73a-ba00c83ccb8a" />

### Для stats:
> INPUT: -m src.lab06.cli_text stats --input data/samples/text.txt --top 5

> OUTPUT: <img width="238" height="113" alt="image" src="https://github.com/user-attachments/assets/09a135e5-89a6-429b-a76a-16f5c1fd9643" />

## Json2csv

```
import argparse
import json
import sys
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main() -> None:
    parser = argparse.ArgumentParser(description="Конвертеры данных JSON / CSV / XLSX")
    sub = parser.add_subparsers(dest="command", required=True)

    # слово in в Python зарезервировано, поэтому сохраняем значение
    # флага --in в поле input (параметр dest)
    p1 = sub.add_parser("json2csv", help="преобразовать JSON в CSV", description="Преобразует JSON в CSV.",)
    p1.add_argument("--in", dest="input", required=True, help="входной .json файл")
    p1.add_argument("--out", dest="output", required=True, help="выходной .csv файл")

    p2 = sub.add_parser("csv2json",help="преобразовать CSV в JSON",description="Преобразует CSV в JSON.",)
    p2.add_argument("--in", dest="input", required=True, help="входной .csv файл")
    p2.add_argument("--out", dest="output", required=True, help="выходной .json файл")

    p3 = sub.add_parser("csv2xlsx",help="преобразовать CSV в XLSX",description="Преобразует CSV в файл Excel.", )
    p3.add_argument("--in", dest="input", required=True, help="входной .csv файл")
    p3.add_argument("--out", dest="output", required=True, help="выходной .xlsx файл")

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        # JSONDecodeError - частный случай ValueError, поэтому его ловим раньше
        print(f"Некорректный JSON",file=sys.stderr,)
        sys.exit(1)
    except ValueError as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        sys.exit(1)

    print(f"Готово: {args.input} -> {args.output}")


if __name__ == "__main__":
    main()

#python3 -m src.lab06.cli_convert json2csv --in data/lab05/csv_json/json.json --out data/lab05/csv_json/result.csv
```



