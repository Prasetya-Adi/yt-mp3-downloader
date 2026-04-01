# 🎵 YouTube to MP3 Downloader (Clean CLI)

A simple and clean Python script to download audio from YouTube videos or playlists and convert them into high-quality MP3 files.

Built using `yt-dlp`, with a minimal and user-friendly command-line output.

---

## ✨ Features

- Download single videos or full playlists
- Convert audio to **MP3 (192 kbps)**
- Resume interrupted downloads
- Automatically skip already downloaded files
- Clean and readable progress output
- Lightweight and fast

---

## 📦 Requirements

Make sure you have:

- Python 3.8+
- FFmpeg installed on your system

## 🔧 Install FFmpeg

### Ubuntu / WSL

sudo apt update
sudo apt install ffmpeg

### macOS (Homebrew)

brew install ffmpeg

### Windows

Download from https://ffmpeg.org/download.html

Check installation:

ffmpeg -version

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Installation

Clone this repository:

```bash
git clone https://github.com/prasetya-adi/ytmp3download.git
cd ytmp3download
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### ▶️ Basic Usage

```bash
python main.py <youtube_url>
```

Example:

```bash
python main.py https://www.youtube.com/playlist?list=XXXX
```

---

### ⌨️ Interactive Mode

If no URL is provided, the script will ask for input:

```bash
python main.py
```

---

## 📂 Output

All downloaded MP3 files will be saved in:

```
downloads/
```

---

## 🖥️ Example Output

```
📦 Total item: 10

🚀 Start downloading...

[1/10] ⬇️ song1.mp3 ... ✅
[2/10] ⏭️ Skip
[3/10] ⬇️ song2.mp3 ... ✅

✅ All done!
```

---

## ⚠️ Notes

- FFmpeg is required for audio conversion
  👉 Make sure it's installed and available in your system PATH

- Already downloaded files will be skipped automatically

- The script uses `yt-dlp`, so it supports many platforms beyond YouTube

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Contribution

Feel free to fork, improve, and submit pull requests!

---

## ⭐ Support

If you find this useful, consider giving it a ⭐ on GitHub!
