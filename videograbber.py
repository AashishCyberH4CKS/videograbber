import yt_dlp
import os

# 🔴 Red text color
def red(text):
    return f"\033[91m{text}\033[0m"

# 🎉 ASCII Header
def print_header():
    banner = """
██╗░░░██╗██╗██████╗░███████╗░█████╗░░██████╗░██████╗░░█████╗░██████╗░██████╗░███████╗██████╗░
██║░░░██║██║██╔══██╗██╔════╝██╔══██╗██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
╚██╗░██╔╝██║██║░░██║█████╗░░██║░░██║██║░░██╗░██████╔╝███████║██████╦╝██████╦╝█████╗░░██████╔╝
░╚████╔╝░██║██║░░██║██╔══╝░░██║░░██║██║░░╚██╗██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝░░██╔══██╗
░░╚██╔╝░░██║██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║██║░░██║██████╦╝██████╦╝███████╗██║░░██║
░░░╚═╝░░░╚═╝╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
"""
    print(red(banner))
    print(red("🔧 Version 1.0 | Created by Aashish_Cyber_H4CKS\n"))

# 🔗 Platform chooser
def get_platform_url():
    print(red("📺 Choose a platform:"))
    print("1️⃣  YouTube")
    print("2️⃣  Instagram (Public Post)")
    print("3️⃣  Facebook (Public Video)")
    
    choice = input("🔢 Enter your choice (1/2/3): ").strip()

    if choice == "1":
        platform = "YouTube"
    elif choice == "2":
        platform = "Instagram"
    elif choice == "3":
        platform = "Facebook"
    else:
        print("❌ Invalid choice.")
        exit()

    url = input(f"🔗 Enter the {platform} video URL: ").strip()
    return url

# 🎵 Format chooser
def get_download_type():
    print(red("\n💽 Choose download type:"))
    print("1️⃣  MP3 (Audio only)")
    print("2️⃣  MP4 (Video + Audio)")

    choice = input("🔢 Enter your choice (1/2): ").strip()
    if choice == "1":
        return "mp3"
    elif choice == "2":
        return "mp4"
    else:
        print("❌ Invalid format choice.")
        exit()

# 📽️ Video quality chooser
def get_quality_format():
    print(red("\n🎞️ Choose MP4 quality:"))
    print("1️⃣  480p")
    print("2️⃣  720p")
    print("3️⃣  1080p")

    choice = input("🔢 Enter your choice (1/2/3): ").strip()
    if choice == "1":
        return 'bestvideo[height<=480]+bestaudio/best[height<=480]'
    elif choice == "2":
        return 'bestvideo[height<=720]+bestaudio/best[height<=720]'
    elif choice == "3":
        return 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
    else:
        print("❌ Invalid quality choice.")
        exit()

# 📥 Downloader
def download_video(url, format_type, quality_format=None):
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    if format_type == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False
        }
        print(red("\n🎧 Downloading MP3... Please wait..."))

    elif format_type == "mp4":
        ydl_opts = {
            'format': quality_format,
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'quiet': False
        }
        print(red("\n📽️  Downloading MP4... Please wait..."))

    else:
        print("❌ Unknown format type.")
        return

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(red("\n✅ Download completed! 📁 Saved in 'downloads' folder."))
    except Exception as e:
        print(red(f"\n❌ Download failed: {e}"))

# 🧠 MAIN
print_header()
print(red("🎉 Welcome to VideoGrabber CLI 🎉"))

url = get_platform_url()
format_type = get_download_type()

if format_type == "mp4":
    quality = get_quality_format()
    download_video(url, "mp4", quality)
else:
    download_video(url, "mp3")
