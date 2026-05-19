class CleanLogger:
    """Menyaring output yt-dlp agar hanya menampilkan info penting."""

    def __init__(self, counter: dict):
        # Menerima dict counter dari luar — lebih aman dari global variable
        self.counter = counter

    def _handle_skip(self):
        """Naikan counter dan print pesan skip."""
        self.counter["current"] += 1
        current = self.counter["current"]
        total = self.counter["total"]
        print(f"[{current}/{total}] ⏭️  Skip (sudah ada)")

    def debug(self, msg: str):
        if "[download] Destination:" in msg:
            self.counter["current"] += 1
            filename = msg.split("Destination:")[-1].strip().split("/")[-1]
            current = self.counter["current"]
            total = self.counter["total"]
            print(f"[{current}/{total}] ⬇️  {filename} ...", end=" ", flush=True)

        elif "has already been downloaded" in msg:
            self._handle_skip()

    def warning(self, msg: str):
        # Pesan skip kadang muncul di warning, bukan debug
        if "has already been downloaded" in msg:
            self._handle_skip()

    def error(self, msg: str):
        print(f"\n❌ Error: {msg}")