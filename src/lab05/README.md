
## Задание A — JSON ↔ CSV

```
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
```

### Для csv_to_json:
> INPUT <img width="118" height="55" alt="image" src="https://github.com/user-attachments/assets/19ff4db4-c2eb-4a3f-b71a-e08d2e84a24d" />

> OUTPUT <img width="319" height="219" alt="image" src="https://github.com/user-attachments/assets/6e86a88a-0482-41a8-be0c-0772794ea7e7" />

### Для json_to_csv:

> INPUT <img width="423" height="69" alt="image" src="https://github.com/user-attachments/assets/5a29ee80-ff21-4518-a6d3-bae9de9cd1a7" />

> OUTPUT <img width="157" height="57" alt="image" src="https://github.com/user-attachments/assets/43036943-0b48-4938-8a9f-2ceebad0cd72" />


## Задание B — CSV → XLSX

```
import pathlib
import csv
import openpyxl 

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX через openpyxl.
    Первая строка CSV — заголовок. Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    path = pathlib.Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
        
    with open(csv_path, "r", encoding="UTF-8", newline="") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        if not rows:
            raise ValueError("CSV-файл пустой или не содержит данных")
            
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    for row in rows:
        ws.append(row)
        
    for col in ws.columns:
        col_letter = col[0].column_letter
        len_cells = []
        for cell in col:
            len_cell = len(str(cell.value))
            len_cells.append(len_cell)
        width = max(8, max(len_cells) + 3)
        ws.column_dimensions[col_letter].width = width
    wb.save(xlsx_path)

if __name__ == "__main__":
    csv_path = "data/lab05/csv_xlsx/csv.csv"
    xlsx_path = "data/lab05/csv_xlsx/xlsx.xlsx"
    csv_to_xlsx(csv_path, xlsx_path)
```

> INPUT <img width="591" height="74" alt="image" src="https://github.com/user-attachments/assets/668f4368-18b6-41e5-9e89-7959ed23a7f6" />

> OUTPUT <img width="920" height="126" alt="image" src="https://github.com/user-attachments/assets/e15043b4-c873-4d6c-b37b-5b1b4fbbeb62" />





