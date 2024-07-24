import os
import yt_dlp

# Function to clean up temporary files
def clean_temp_files(directory, title):
    extensions = ['.webm', '.mkv', '.mp4']
    for ext in extensions:
        temp_file = os.path.join(directory, f"{title}{ext}")
        if os.path.exists(temp_file) and ext != '.mp4':
            os.remove(temp_file)

youtube_url = 'https://www.youtube.com/watch?v=WC08trrozPs'
save_dir = 'Downloaded_videos'
os.makedirs(save_dir, exist_ok=True)

ydl_opts = {
    'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s'),
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Ensure this is 'preferedformat' and not 'preferredformat'
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    result = ydl.extract_info(youtube_url)
    title = result['title']
    # Clean up temporary files after download
    clean_temp_files(save_dir, title)
