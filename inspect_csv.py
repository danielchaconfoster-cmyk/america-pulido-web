import csv
from pathlib import Path

csv_path = Path(__file__).parent / "calendario_6_semanas_america_pulido.csv"

with open(csv_path, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header columns:", header)
    first_row = next(reader)
    print("First row len:", len(first_row))
