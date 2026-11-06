import pathlib
import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8.
    """
    path = pathlib.Path(json_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")
    
    with open(json_path, "r", encoding="UTF-8") as f:
        try:
            jsn = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Некорректный формат JSON")
            
    if not isinstance(jsn, list) or not jsn:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(item, dict) for item in jsn):
        raise ValueError("Элементы JSON должны быть словарями")
        
    fieldnames = list(jsn[0].keys())
    
    with open(csv_path, "w", encoding="UTF-8", newline="") as r:
        writer = csv.DictWriter(r, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(jsn)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    """
    path = pathlib.Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
        
    with open(csv_path, "r", encoding="UTF-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        
        if not rows or not reader.fieldnames:
            raise ValueError("CSV-файл пустой, отсутствует заголовок или нет данных")
            
    with open(json_path, "w", encoding="UTF-8") as json_file:
        json.dump(rows, json_file, ensure_ascii=False, indent=2)
        
if __name__ == "__main__":
    # Этот код выполнится ТОЛЬКО если файл запустили напрямую через терминал.
    # Если файл просто импортировали — этот блок будет пропущен.
    json_path_1 = "data/lab05/json.json"
    csv_path_1 = "data/lab05/result.csv"

    csv_path_2 = "data/lab05/csv_json/csv.csv"
    json_path_2 = "data/lab05/csv_json/result.json"
    #json_to_csv(json_path_1,csv_path_1)
    csv_to_json(csv_path_2, json_path_2)

