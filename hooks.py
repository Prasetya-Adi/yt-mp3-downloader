def progress_hook(d: dict):
    """
    Dipanggil yt-dlp setiap kali status download berubah.
    Bisa ditambah hook lain di sini nanti (misal: logging ke file).
    """
    if d["status"] == "finished":
        print("✅")
    elif d["status"] == "error":
        print("❌ Gagal!")