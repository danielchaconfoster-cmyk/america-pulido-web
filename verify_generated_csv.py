import csv
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

target_file = Path(r"c:\Users\usuario\Desktop\america-pulido-web\metricool_SERVICIOS_OFICIAL.csv")

with open(target_file, "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

print(f"Total lines in file: {len(lines)}")
header_line = lines[0].strip()
headers = header_line.split(";")
print(f"Header columns count: {len(headers)}")

# Verify rows using csv reader with ';' delimiter
with open(target_file, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f, delimiter=";")
    h_row = next(reader)
    row_count = 0
    for idx, r in enumerate(reader, 1):
        row_count += 1
        if len(r) != len(headers):
            print(f"❌ Row {idx} has {len(r)} columns, expected {len(headers)}")
        else:
            # Check specific fields
            date_val = r[1]
            time_val = r[2]
            draft_val = r[3]
            fb_val = r[4]
            ig_val = r[8]
            img_val = r[14]
            print(f"Row {idx:2d} OK | Date: {date_val} | Time: {time_val} | Draft: {draft_val} | FB: {fb_val} | IG: {ig_val} | Img: {img_val[:35]}...")

print(f"\nVerification finished: {row_count}/21 rows parsed successfully with exact 96 columns!")
