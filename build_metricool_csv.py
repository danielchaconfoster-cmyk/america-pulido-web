import csv
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

csv_path = Path(__file__).parent / "calendario_6_semanas_america_pulido.csv"

HEADER_STR = "Text;Date;Time;Draft;Facebook;Twitter/X;LinkedIn;GBP;Instagram;Pinterest;TikTok;Youtube;Threads;Bluesky;Picture Url 1;Picture Url 2;Picture Url 3;Picture Url 4;Picture Url 5;Picture Url 6;Picture Url 7;Picture Url 8;Picture Url 9;Picture Url 10;Alt text picture 1;Alt text picture 2;Alt text picture 3;Alt text picture 4;Alt text picture 5;Alt text picture 6;Alt text picture 7;Alt text picture 8;Alt text picture 9;Alt text picture 10;Document title;Shortener;Video Thumbnail Url;Video Cover Frame;Twitter/X Can reply;Twitter/X Type;Twitter/X Poll Duration minutes;Twitter/X Poll Option 1;Twitter/X Poll Option 2;Twitter/X Poll Option 3;Twitter/X Poll Option 4;Pinterest Board;Pinterest Pin Title;Pinterest Pin Link;Pinterest Pin New Format;Instagram Post Type;Instagram Show Reel On Feed;Instagram Trial Reel Share Automatically;Youtube Video Title;Youtube Video Type;Youtube Video Privacy;Youtube video for kids;Youtube AI generated content;Youtube Video Category;Youtube Video Tags;Youtube playlist;GBP Post Type;Facebook Post Type;Facebook Title;First Comment Text;TikTok Title;TikTok disable comments;TikTok disable duet;TikTok disable stitch;TikTok Post Privacy;TikTok Branded Content;TikTok Your Brand;TikTok Auto Add Music;TikTok Photo Cover Index;TikTok musicId;TikTok music title;TikTok music author;TikTok music previewUrl;TikTok music thumbnailUrl;TikTok music soundVolume;TikTok music originalVolume;TikTok music startMillis;TikTok music endMillis;TikTok Ai generated content;LinkedIn Type;LinkedIn Poll Question;LinkedIn Poll Option 1;LinkedIn Poll Option 2;LinkedIn Poll Option 3;LinkedIn Poll Option 4;LinkedIn Poll Duration;LinkedIn Show link preview;LinkedIn Images as Carousel;Threads Reply Control;Threads Is Spoiler;Threads Post Type;Brand name"

headers = HEADER_STR.split(";")

entries = []
with open(csv_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        datetime_str = row["Date and time"].strip()
        date_part, time_part = datetime_str.split(" ")
        text = row["Text"].strip()
        img_url = row["Image URL"].strip()
        
        yyyy, mm, dd = date_part.split("-")
        yy = yyyy[-2:] # "26"
        
        # Ensure time has HH:MM:SS format
        if len(time_part) == 5:
            time_part = f"{time_part}:00"
            
        entries.append({
            "date_ymd": f"{yyyy}-{mm}-{dd}",       # 2026-08-26
            "date_dmy_4": f"{dd}/{mm}/{yyyy}",    # 26/08/2026
            "date_dmy_2": f"{dd}/{mm}/{yy}",      # 26/08/26
            "time": time_part,                    # 20:00:00
            "text": text,
            "image": img_url
        })

def make_csv(filename, date_key):
    out_path = Path(__file__).parent / filename
    rows = []
    for entry in entries:
        row_dict = {h: "" for h in headers}
        
        row_dict["Text"] = entry["text"]
        row_dict["Date"] = entry[date_key]
        row_dict["Time"] = entry["time"]
        row_dict["Draft"] = "false"
        row_dict["Facebook"] = "true"
        row_dict["Twitter/X"] = "false"
        row_dict["LinkedIn"] = "false"
        row_dict["GBP"] = "false"
        row_dict["Instagram"] = "true"
        row_dict["Pinterest"] = "false"
        row_dict["TikTok"] = "false"
        row_dict["Youtube"] = "false"
        row_dict["Threads"] = "false"
        row_dict["Bluesky"] = "false"
        row_dict["Picture Url 1"] = entry["image"]
        row_dict["Shortener"] = "true"
        row_dict["Instagram Post Type"] = "POST"
        row_dict["Facebook Post Type"] = "POST"
        row_dict["TikTok Post Privacy"] = "PUBLIC_TO_EVERYONE"
        row_dict["TikTok disable comments"] = "false"
        row_dict["TikTok disable duet"] = "false"
        row_dict["TikTok disable stitch"] = "false"
        row_dict["TikTok Branded Content"] = "false"
        row_dict["TikTok Your Brand"] = "false"
        row_dict["TikTok Auto Add Music"] = "false"
        row_dict["TikTok Photo Cover Index"] = "0"
        row_dict["TikTok Ai generated content"] = "false"
        
        rows.append(row_dict)

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
        for r in rows:
            row_vals = [r[h] for h in headers]
            writer.writerow(row_vals)
    print(f"Generado {filename}")

make_csv("metricool_DD_MM_YY.csv", "date_dmy_2")      # 26/08/26
make_csv("metricool_DD_MM_YYYY.csv", "date_dmy_4")    # 26/08/2026
make_csv("metricool_YYYY_MM_DD.csv", "date_ymd")      # 2026-08-26

print("Todos los archivos CSV generados correctamente.")
