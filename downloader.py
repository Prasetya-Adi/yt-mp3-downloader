import yt_dlp
from logger import CleanLogger
from hooks import progress_hook
from utils import prepare_output_folder


def get_total_items(url: str) -> int:
    """Ambil jumlah item dari URL tanpa download (ringan)."""
    with yt_dlp.YoutubeDL({"quiet": True, "extract_flat": True}) as ydl:
        info = ydl.extract_info(url, download=False)
        return len(info["entries"]) if "entries" in info else 1


def build_ydl_opts(output_path: str, counter: dict) -> dict:
    """
    Bangun konfigurasi yt-dlp.
    Dipisah ke fungsi sendiri agar mudah diubah atau di-test.
    """
    return {
        "format": "bestaudio/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "noplaylist": False,
        "overwrites": False,
        "ignoreerrors": True,
        "quiet": True,
        "no_warnings": True,
        "logger": CleanLogger(counter),
        "progress_hooks": [progress_hook],
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }


def download_mp3(url: str, output_path: str = "downloads"):
    """Download audio dari URL dan simpan sebagai MP3 192kbps."""
    output_path = prepare_output_folder(output_path)

    print("🔍 Mengambil info playlist/video...")
    total_items = get_total_items(url)
    print(f"📦 Total item: {total_items}\n")

    # Dict karena bisa dimodifikasi di dalam CleanLogger (int tidak bisa)
    counter = {"current": 0, "total": total_items}

    ydl_opts = build_ydl_opts(output_path, counter)

    print("🚀 Mulai download...\n")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\n✅ Semua selesai!")