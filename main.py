import os
import yt_dlp

cur_dir = os.getcwd()

def download_video(link, id):
    youtube_dl_options = {
        'format_sort': ['res:1080', 'ext:mp4:m4a'],
        "outtmpl": os.path.join(cur_dir, f"{id}.mp4"),
    }

    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        return ydl.download([link])

def download_audio(link, id):
    youtube_dl_options = {
        "format": "ba",  # This will select the specific resolution typed here
        "outtmpl": os.path.join(cur_dir, f"{id}.mp3"),
    }

    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        return ydl.download([link])

# Get the YouTube URL from the user
youtube_url = input("Enter the YouTube URL: ")

# Choose whether to download video or audio
choice = input("Enter 'v' to download video or 'a' to download audio: ")

if choice == 'v':
    download_video(youtube_url, 'video_id')
elif choice == 'a':
    download_audio(youtube_url, 'audio_id')
else:
    print("Invalid choice. Please enter 'v' for video or 'a' for audio.")

