
## Задание A — модуль src/lab04/io_txt_csv.py

```
import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текстовый файл и возвращает его содержимое одной строкой.
    
    #Пример другой кодировки: read_text("file.txt", encoding="cp1251
    #return Path(path).read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    #Создаёт родительские папки для файла, если их ещё нет.
    #Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    #Создаёт или перезаписывает CSV-файл (разделитель ',', UTF-8).
    ensure_parent_dir(path)
    rows = list(rows)
    if rows:
        width = len(rows[0])
        for r in rows:
            if len(r) != width:
                raise ValueError(
                    f"Строки разной длины: ожидалось {width}, получено {len(r)}"
                )

    with Path(path).open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```
## Задание B — скрипт src/lab04/text_report.py

```
import pathlib
import sys
import csv
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from lib.text import tokenize, count_freq, top_n, normalize
from io_txt_csv import write_csv, read_text


def text_report(path: str | pathlib.Path, encoding: str = "utf-8"):
    
    p = pathlib.Path(path)
    
    if not p.exists():
        print(f"Ошибка: входной файл '{p}' не найден.", file=sys.stderr)
        sys.exit(1)
    try:
        raw_text = read_text(p, encoding=encoding)
    except UnicodeDecodeError as e:
        print(f"Ошибка декодирования файла '{p}' ({encoding}): {e}. "
              f"Укажите корректную кодировку (например, --encoding cp1251).", file=sys.stderr)
        sys.exit(1)

    text = normalize(p.read_text(encoding = "utf-8"))
    tokens = tokenize(text)
    freq = count_freq(tokens)
    top = top_n(freq)
    sorted_top = top
    
    write_csv(
    rows= sorted_top, 
    path="data/lab04/report.csv", 
    header=("word", "count")
    )
    with open("data/lab04/result.csv","w") as f:
        w = csv.writer(f)
        w.writerow([f"Кол-во слов: {len(tokens)}"])
        w.writerow([f"Уникальных слов: {len(freq)}"])
        w.writerow(["Топ-5:"])
         # Открываем второй файл для чтения
        with open('data/lab04/report.csv', mode='r', newline='', encoding='utf-8') as f2:
            reader = csv.reader(f2)
            for i in reader:
                w.writerow(i)
    return read_text("data/lab04/result.csv")


if __name__ == "__main__":
    input_path = "data/lab04/input.txt"
    file_encoding = "utf-8"

    print(text_report(input_path, encoding=file_encoding))
```
> INPUT: <img width="658" height="32" alt="image" src="https://github.com/user-attachments/assets/7c6bac8c-678b-4ae8-8cba-c3d4a3f53b83" />

> 

> OUTPUT: <img width="739" height="129" alt="image" src="https://github.com/user-attachments/assets/c16037f4-c93d-4a28-a360-7769bf47fa7e" />
