# 🎵 YouTube to MP3 Downloader (Clean CLI)

A simple and clean Python CLI tool to download audio from YouTube videos or playlists and convert them into high-quality MP3 files.

Built using `yt-dlp`, with minimal and readable command-line output.

---

## ✨ Features

- Download single videos or full playlists
- Convert audio to **MP3 (192 kbps)**
- Resume interrupted downloads
- Automatically skip already downloaded files
- Clean and readable progress output
- Lightweight and fast

---

## 📁 Project Structure

```
ytmp3download/
├── main.py          # Entry point — run this file
├── downloader.py    # Core download logic
├── logger.py        # Custom output filter for yt-dlp
├── hooks.py         # Progress hooks (status: finished / error)
├── utils.py         # URL validation and folder helper
└── requirements.txt
```

---

## 📦 Requirements

- Python 3.8+
- FFmpeg installed on your system

### Install FFmpeg

**Ubuntu / WSL**

```bash
sudo apt update && sudo apt install ffmpeg
```

**macOS (Homebrew)**

```bash
brew install ffmpeg
```

**Windows**
Download from https://ffmpeg.org/download.html

Verify installation:

```bash
ffmpeg -version
```

---

## ⚙️ Installation

Clone this repository:

```bash
git clone https://github.com/prasetya-adi/ytmp3download.git
cd ytmp3download
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Basic usage

```bash
python main.py <youtube_url>
```

Example — single video:

```bash
python main.py https://www.youtube.com/watch?v=XXXX
```

Example — playlist:

```bash
python main.py https://www.youtube.com/playlist?list=XXXX
```

### Interactive mode

If no URL is provided, the script will prompt for input:

```bash
python main.py
```

---

## 📂 Output

All MP3 files will be saved to:

```
downloads/
```

---

## 🖥️ Example Output

```
🔍 Mengambil info playlist/video...
📦 Total item: 10

🚀 Mulai download...

[1/10] ⬇️  Song Title 1.webm ... ✅
[2/10] ⏭️  Skip (sudah ada)
[3/10] ⬇️  Song Title 2.webm ... ✅

✅ Semua selesai!
```

> Note: The filename shown during download reflects the original format before conversion.
> The final saved file will be `.mp3`.

---

## ⚠️ Notes

- FFmpeg must be installed and available in your system `PATH` for audio conversion to work
- Already downloaded files are skipped automatically
- If a video is unavailable (private, geo-blocked, etc.), it will be skipped and the download will continue
- `yt-dlp` supports many platforms beyond YouTube

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Contribution

Feel free to fork, improve, and submit pull requests!

---

## ⭐ Support

If you find this useful, consider giving it a ⭐ on GitHub!
