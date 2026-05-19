import os

def validate_url(url: str) -> str:
    """Validasi dan bersihkan URL input dari user."""
    url = url.strip()
    if not url:
        raise ValueError("URL tidak boleh kosong.")
    return url

def prepare_output_folder(path: str) -> str:
    """Normalisasi path dan buat folder jika belum ada."""
    path = os.path.normpath(path)
    os.makedirs(path, exist_ok=True)
    return path