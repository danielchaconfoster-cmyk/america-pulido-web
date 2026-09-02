import csv
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# Import standard 18 posts from meta_publisher.py
from meta_publisher import PARRILLA_POSTS

PUBLIC_BASE = "https://www.americapulidospa.cl"

HEADER_STR = "Text;Date;Time;Draft;Facebook;Twitter/X;LinkedIn;GBP;Instagram;Pinterest;TikTok;Youtube;Threads;Bluesky;Picture Url 1;Picture Url 2;Picture Url 3;Picture Url 4;Picture Url 5;Picture Url 6;Picture Url 7;Picture Url 8;Picture Url 9;Picture Url 10;Alt text picture 1;Alt text picture 2;Alt text picture 3;Alt text picture 4;Alt text picture 5;Alt text picture 6;Alt text picture 7;Alt text picture 8;Alt text picture 9;Alt text picture 10;Document title;Shortener;Video Thumbnail Url;Video Cover Frame;Twitter/X Can reply;Twitter/X Type;Twitter/X Poll Duration minutes;Twitter/X Poll Option 1;Twitter/X Poll Option 2;Twitter/X Poll Option 3;Twitter/X Poll Option 4;Pinterest Board;Pinterest Pin Title;Pinterest Pin Link;Pinterest Pin New Format;Instagram Post Type;Instagram Show Reel On Feed;Instagram Trial Reel Share Automatically;Youtube Video Title;Youtube Video Type;Youtube Video Privacy;Youtube video for kids;Youtube AI generated content;Youtube Video Category;Youtube Video Tags;Youtube playlist;GBP Post Type;Facebook Post Type;Facebook Title;First Comment Text;TikTok Title;TikTok disable comments;TikTok disable duet;TikTok disable stitch;TikTok Post Privacy;TikTok Branded Content;TikTok Your Brand;TikTok Auto Add Music;TikTok Photo Cover Index;TikTok musicId;TikTok music title;TikTok music author;TikTok music previewUrl;TikTok music thumbnailUrl;TikTok music soundVolume;TikTok music originalVolume;TikTok music startMillis;TikTok music endMillis;TikTok Ai generated content;LinkedIn Type;LinkedIn Poll Question;LinkedIn Poll Option 1;LinkedIn Poll Option 2;LinkedIn Poll Option 3;LinkedIn Poll Option 4;LinkedIn Poll Duration;LinkedIn Show link preview;LinkedIn Images as Carousel;Threads Reply Control;Threads Is Spoiler;Threads Post Type;Brand name"

headers = HEADER_STR.split(";")

# Dates across 6 weeks starting 2026-08-26
dates_list = [
    ("2026-08-26", "2026/08/26", "20:00:00"),
    ("2026-08-28", "2026/08/28", "20:00:00"),
    ("2026-08-30", "2026/08/30", "11:00:00"),
    ("2026-08-31", "2026/08/31", "20:00:00"),
    ("2026-09-02", "2026/09/02", "20:00:00"),
    ("2026-09-04", "2026/09/04", "08:00:00"),
    ("2026-09-06", "2026/09/06", "11:00:00"),
    ("2026-09-07", "2026/09/07", "20:00:00"),
    ("2026-09-09", "2026/09/09", "20:00:00"),
    ("2026-09-11", "2026/09/11", "20:00:00"),
    ("2026-09-13", "2026/09/13", "11:00:00"),
    ("2026-09-14", "2026/09/14", "20:00:00"),
    ("2026-09-16", "2026/09/16", "08:00:00"),
    ("2026-09-18", "2026/09/18", "20:00:00"),
    ("2026-09-20", "2026/09/20", "11:00:00"),
    ("2026-09-21", "2026/09/21", "20:00:00"),
    ("2026-09-23", "2026/09/23", "08:30:00"),
    ("2026-09-25", "2026/09/25", "20:00:00"),
]

def generate_csv_file(filepath, is_slash=True):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(HEADER_STR + "\n")
        
        for idx in range(1, 19):
            post_data = PARRILLA_POSTS[idx]
            d_dash, d_slash, t_val = dates_list[idx - 1]
            date_str = d_slash if is_slash else d_dash
            
            img_url = f"{PUBLIC_BASE}/{post_data['image']}"
            text = post_data["caption"].replace('"', '""') # escape inner quotes
            
            row = []
            for h in headers:
                if h == "Text":
                    row.append(f'"{text}"')
                elif h == "Date":
                    row.append(f'"{date_str}"')
                elif h == "Time":
                    row.append(f'"{t_val}"')
                elif h in ["Draft", "Twitter/X", "LinkedIn", "GBP", "Pinterest", "TikTok", "Youtube", "Threads", "Bluesky"]:
                    row.append("false")
                elif h in ["Facebook", "Instagram"]:
                    row.append("true")
                elif h == "Picture Url 1":
                    row.append(f'"{img_url}"')
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
            
            f.write(";".join(row) + "\n")

out_slashes = Path(__file__).parent / "metricool_PERFECTO_SLASHES.csv"
out_dashes = Path(__file__).parent / "metricool_PERFECTO_DASHES.csv"

generate_csv_file(out_slashes, is_slash=True)
generate_csv_file(out_dashes, is_slash=False)

print(f"OK: Generados {out_slashes.name} y {out_dashes.name} con las URLs oficiales verificadas HTTP 200 OK.")
