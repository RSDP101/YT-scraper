import yt_dlp as youtube_dl
import csv
import argparse

def scrape(query, count):
    # Function to search YouTube for shorts
    def search_youtube(query, count):
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'noplaylist': True,
            'extract_flat': 'in_playlist',
            'dump_single_json': True
        }
        search_url = f"ytsearch{count}:{query} short"
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(search_url, download=False)
            return result['entries']

    # Search YouTube
    shorts = search_youtube(query, count)

    # Create a CSV file and write the results
    with open('youtube_shorts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URLs'])
        
        for short in shorts:
            writer.writerow([short['url']])

    print("YouTube Shorts URLs saved to youtube_shorts.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search and download YouTube Shorts URLs based on a query.")
    parser.add_argument("--query", type=str, required=True, help="The search query to find YouTube Shorts.")
    parser.add_argument("--count", type=int, required=True, help="The number of results to return.")
    args = parser.parse_args()
    scrape(args.query, args.count)
