import csv
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

csv_path = Path(__file__).parent / "calendario_6_semanas_america_pulido.csv"
output_dashes = Path(__file__).parent / "metricool_DASHES_YYYY-MM-DD.csv"
output_slashes = Path(__file__).parent / "metricool_SLASHES_YYYY_MM_DD.csv"

# Header oficial exacto de la plantilla de Metricool
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
        
        if len(time_part) == 5:
            time_part = f"{time_part}:00"
            
        entries.append({
            "date_dash": f"{yyyy}-{mm}-{dd}",   # 2026-08-26
            "date_slash": f"{yyyy}/{mm}/{dd}",  # 2026/08/26
            "time": time_part,                  # 20:00:00
            "text": text,
            "image": img_url
        })

# Format a value strictly according to Metricool's sample line:
# Booleans: unquoted true/false
# Strings: double quoted
def format_metricool_row(entry, date_key):
    row = []
    for h in headers:
        if h == "Text":
            row.append(f'"{entry["text"]}"')
        elif h == "Date":
            row.append(f'"{entry[date_key]}"')
        elif h == "Time":
            row.append(f'"{entry["time"]}"')
        elif h in ["Draft", "Twitter/X", "LinkedIn", "GBP", "Pinterest", "TikTok", "Youtube", "Threads", "Bluesky"]:
            row.append("false")
        elif h in ["Facebook", "Instagram"]:
            row.append("true")
        elif h == "Picture Url 1":
            row.append(f'"{entry["image"]}"')
        elif h in ["Picture Url 2", "Picture Url 3", "Picture Url 4", "Picture Url 5"]:
            row.append('""')
        elif h == "Shortener":
            row.append("true")
        elif h in ["Pinterest Pin New Format", "Youtube video for kids", "Youtube AI generated content",
                   "TikTok disable comments", "TikTok disable duet", "TikTok disable stitch",
                   "TikTok Branded Content", "TikTok Your Brand", "TikTok Auto Add Music",
                   "TikTok Ai generated content", "LinkedIn Show link preview", "LinkedIn Images as Carousel",
                   "Threads Is Spoiler"]:
            row.append("false")
        elif h == "Instagram Post Type":
            row.append('"POST"')
        elif h == "Facebook Post Type":
            row.append('"POST"')
        elif h == "TikTok Post Privacy":
            row.append('"PUBLIC_TO_EVERYONE"')
        elif h == "TikTok Photo Cover Index":
            row.append('"0"')
        else:
            row.append('""')
    return ";".join(row)

# Write Dashes File
with open(output_dashes, "w", encoding="utf-8") as f:
    f.write(HEADER_STR + "\n")
    for entry in entries:
        f.write(format_metricool_row(entry, "date_dash") + "\n")

# Write Slashes File
with open(output_slashes, "w", encoding="utf-8") as f:
    f.write(HEADER_STR + "\n")
    for entry in entries:
        f.write(format_metricool_row(entry, "date_slash") + "\n")

print(f"OK: Generados {output_dashes.name} y {output_slashes.name} exactamente igual a la muestra de Metricool.")
