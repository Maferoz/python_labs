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
