import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Load extracted posts
json_path = Path(r"c:\Users\usuario\Desktop\america-pulido-web\extracted_servicios_posts.json")
with open(json_path, "r", encoding="utf-8") as f:
    posts = json.load(f)

HEADER_STR = "Text;Date;Time;Draft;Facebook;Twitter/X;LinkedIn;GBP;Instagram;Pinterest;TikTok;Youtube;Threads;Bluesky;Picture Url 1;Picture Url 2;Picture Url 3;Picture Url 4;Picture Url 5;Picture Url 6;Picture Url 7;Picture Url 8;Picture Url 9;Picture Url 10;Alt text picture 1;Alt text picture 2;Alt text picture 3;Alt text picture 4;Alt text picture 5;Alt text picture 6;Alt text picture 7;Alt text picture 8;Alt text picture 9;Alt text picture 10;Document title;Shortener;Video Thumbnail Url;Video Cover Frame;Twitter/X Can reply;Twitter/X Type;Twitter/X Poll Duration minutes;Twitter/X Poll Option 1;Twitter/X Poll Option 2;Twitter/X Poll Option 3;Twitter/X Poll Option 4;Pinterest Board;Pinterest Pin Title;Pinterest Pin Link;Pinterest Pin New Format;Instagram Post Type;Instagram Show Reel On Feed;Instagram Trial Reel Share Automatically;Youtube Video Title;Youtube Video Type;Youtube Video Privacy;Youtube video for kids;Youtube AI generated content;Youtube Video Category;Youtube Video Tags;Youtube playlist;GBP Post Type;Facebook Post Type;Facebook Title;First Comment Text;TikTok Title;TikTok disable comments;TikTok disable duet;TikTok disable stitch;TikTok Post Privacy;TikTok Branded Content;TikTok Your Brand;TikTok Auto Add Music;TikTok Photo Cover Index;TikTok musicId;TikTok music title;TikTok music author;TikTok music previewUrl;TikTok music thumbnailUrl;TikTok music soundVolume;TikTok music originalVolume;TikTok music startMillis;TikTok music endMillis;TikTok Ai generated content;LinkedIn Type;LinkedIn Poll Question;LinkedIn Poll Option 1;LinkedIn Poll Option 2;LinkedIn Poll Option 3;LinkedIn Poll Option 4;LinkedIn Poll Duration;LinkedIn Show link preview;LinkedIn Images as Carousel;Threads Reply Control;Threads Is Spoiler;Threads Post Type;Brand name"

headers = HEADER_STR.split(";")

BOOLEAN_FIELDS = {
    "Draft", "Facebook", "Twitter/X", "LinkedIn", "GBP", "Instagram", "Pinterest",
    "TikTok", "Youtube", "Threads", "Bluesky", "Shortener", "Pinterest Pin New Format",
    "Youtube video for kids", "Youtube AI generated content", "TikTok disable comments",
    "TikTok disable duet", "TikTok disable stitch", "TikTok Branded Content",
    "TikTok Your Brand", "TikTok Auto Add Music", "TikTok Ai generated content",
    "LinkedIn Show link preview", "LinkedIn Images as Carousel", "Threads Is Spoiler"
}

def format_date(date_str, mode):
    # date_str is YYYY-MM-DD
    yyyy, mm, dd = date_str.split('-')
    if mode == "YYYY/MM/DD":
        return f"{yyyy}/{mm}/{dd}"
    elif mode == "YYYY-MM-DD":
        return f"{yyyy}-{mm}-{dd}"
    elif mode == "DD/MM/YYYY":
        return f"{dd}/{mm}/{yyyy}"
    elif mode == "DD-MM-YYYY":
        return f"{dd}-{mm}-{yyyy}"
    return date_str

def create_metricool_csv(target_path, date_mode="YYYY/MM/DD", include_seconds=True):
    with open(target_path, "w", encoding="utf-8-sig") as f:
        f.write(HEADER_STR + "\n")
        
        for post in posts:
            d_val = format_date(post["date"], date_mode)
            t_val = post["time"] if include_seconds else post["time"][:5]
            img_url = post["img_url"]
            text_val = post["text"].replace('"', '""') # escape inner quotes
            
            row = []
            for h in headers:
                if h == "Text":
                    row.append(f'"{text_val}"')
                elif h == "Date":
                    row.append(f'"{d_val}"')
                elif h == "Time":
                    row.append(f'"{t_val}"')
                elif h == "Picture Url 1":
                    row.append(f'"{img_url}"')
                elif h in ["Facebook", "Instagram"]:
                    row.append("true")
                elif h == "Shortener":
                    row.append("true")
                elif h in BOOLEAN_FIELDS:
                    row.append("false")
                elif h in ["Instagram Post Type", "Facebook Post Type"]:
                    row.append('"POST"')
                elif h == "TikTok Post Privacy":
                    row.append('"PUBLIC_TO_EVERYONE"')
                elif h == "TikTok Photo Cover Index":
                    row.append('"0"')
                else: # All other string fields
                    row.append('""')
            
            f.write(";".join(row) + "\n")
    print(f"Generated: {target_path.name} ({target_path.stat().st_size} bytes)")

base_dir = Path(r"c:\Users\usuario\Desktop\america-pulido-web")

# Generate different date format variants for user convenience
file1 = base_dir / "metricool_SERVICIOS_YYYY_MM_DD_slashes.csv"
file2 = base_dir / "metricool_SERVICIOS_YYYY_MM_DD_dashes.csv"
file3 = base_dir / "metricool_SERVICIOS_DD_MM_YYYY_slashes.csv"
file4 = base_dir / "metricool_SERVICIOS_OFICIAL.csv"

create_metricool_csv(file1, date_mode="YYYY/MM/DD", include_seconds=True)
create_metricool_csv(file2, date_mode="YYYY-MM-DD", include_seconds=True)
create_metricool_csv(file3, date_mode="DD/MM/YYYY", include_seconds=True)
create_metricool_csv(file4, date_mode="YYYY/MM/DD", include_seconds=True)

print("All Metricool CSVs generated successfully.")
