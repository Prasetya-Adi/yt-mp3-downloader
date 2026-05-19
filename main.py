import yt_dlp
import os
import sys


# =========================
# Logger
# =========================
class CleanLogger:
    """Menyaring output yt-dlp agar hanya menampilkan info penting."""

    def __init__(self, counter):
        # Menerima counter dari luar agar tidak pakai global variable
        self.counter = counter

    def debug(self, msg):
        # Deteksi: mulai download file baru
        if "[download] Destination:" in msg:
            self.counter["current"] += 1
            filename = msg.split("Destination:")[-1].strip().split("/")[-1]
            total = self.counter["total"]
            current = self.counter["current"]
            print(f"[{current}/{total}] ⬇️  {filename} ...", end=" ", flush=True)

        # Deteksi: file sudah ada, di-skip
        elif "has already been downloaded" in msg:
            self.counter["current"] += 1
            total = self.counter["total"]
            current = self.counter["current"]
            print(f"[{current}/{total}] ⏭️  Skip (sudah ada)")

    def warning(self, msg):
        # Tampilkan warning skip yang kadang muncul di sini
        if "has already been downloaded" in msg:
            self.debug(msg)  # Arahkan ke handler yang sama

    def error(self, msg):
        print(f"\n❌ Error: {msg}")


# =========================
# Progress Hook
# =========================
def progress_hook(d):
    """Dipanggil yt-dlp saat status download berubah."""
    if d["status"] == "finished":
        print("✅")
    elif d["status"] == "error":
        print("❌ Gagal!")


# =========================
# Main Function
# =========================
def download_mp3(url, output_path="downloads"):
    """
    Download audio dari URL (video tunggal atau playlist)
    dan simpan sebagai MP3 192kbps.
    """

    # Validasi sederhana agar output_path tidak keluar dari direktori kerja
    output_path = os.path.normpath(output_path)
    os.makedirs(output_path, exist_ok=True)

    # -------------------------------------------------
    # Tahap 1: Hitung total item tanpa download
    # -------------------------------------------------
    print("🔍 Mengambil info playlist/video...")

    with yt_dlp.YoutubeDL({"quiet": True, "extract_flat": True}) as ydl:
        info = ydl.extract_info(url, download=False)
        total_items = len(info["entries"]) if "entries" in info else 1

    print(f"📦 Total item: {total_items}\n")

    # Counter pakai dict agar bisa dimodifikasi di dalam CleanLogger
    # (dict di-pass by reference, int tidak)
    counter = {"current": 0, "total": total_items}

    # -------------------------------------------------
    # Tahap 2: Download
    # -------------------------------------------------
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "noplaylist": False,

        # Jangan timpa file yang sudah ada
        "overwrites": False,

        # Lanjutkan download yang terputus (default True, ditulis eksplisit)
        "noprogress": False,

        # Tetap lanjut meski ada 1 video yang error
        "ignoreerrors": True,

        # Sembunyikan output bawaan yt-dlp
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

    print("🚀 Mulai download...\n")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\n✅ Semua selesai!")


# =========================
# Entry Point
# =========================
if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Masukkan URL video / playlist: ").strip()

    if not url:
        print("❌ URL tidak boleh kosong.")
        sys.exit(1)

    download_mp3(url)