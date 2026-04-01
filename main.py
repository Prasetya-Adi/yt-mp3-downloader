import yt_dlp, os, sys

# =========================
# Global Counter
# =========================
current_index = 0
total_items = 0


# =========================
# Logger
# =========================
class CleanLogger:
    def debug(self, msg):
        global current_index

        # Detect start download
        if "[download] Destination:" in msg:
            current_index += 1
            title = msg.split("Destination:")[-1].strip().split("/")[-1]

            print(f"[{current_index}/{total_items}] ⬇️ {title} ...", end=" ")

        # Detect skip
        elif "has already been downloaded" in msg:
            current_index += 1
            print(f"[{current_index}/{total_items}] ⏭️ Skip")

    def warning(self, msg):
        pass

    def error(self, msg):
        print(f"\n❌ Error: {msg}")


# =========================
# Progress Hook
# =========================
def progress_hook(d):
    if d['status'] == 'finished':
        print("✅")


# =========================
# Main Function
# =========================
def download_mp3(url, output_path="downloads"):
    global total_items

    os.makedirs(output_path, exist_ok=True)

    # 🔥 Ambil total item SAJA (ringan)
    with yt_dlp.YoutubeDL({'quiet': True, 'extract_flat': True}) as ydl:
        info = ydl.extract_info(url, download=False)

        if 'entries' in info:
            total_items = len(info['entries'])
        else:
            total_items = 1

    print(f"\n📦 Total item: {total_items}\n")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',

        'noplaylist': False,

        # resumable
        'continuedl': True,

        # skip otomatis
        'overwrites': False,
        'ignoreerrors': True,

        # clean output
        'quiet': True,
        'no_warnings': True,

        'logger': CleanLogger(),
        'progress_hooks': [progress_hook],

        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    print("🚀 Start downloading...\n")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\n✅ All done!")


# =========================
# Entry
# =========================

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Masukkan URL video / playlist: ")

    download_mp3(url)