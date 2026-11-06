import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текстовый файл и возвращает его содержимое одной строкой.
    
    Пример другой кодировки: read_text("file.txt", encoding="cp1251")
    """
    return Path(path).read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские папки для файла, если их ещё нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Создаёт или перезаписывает CSV-файл (разделитель ',', UTF-8).
    """
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