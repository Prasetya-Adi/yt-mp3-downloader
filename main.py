import sys
from utils import validate_url
from downloader import download_mp3


def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Masukkan URL video / playlist: ")

    try:
        url = validate_url(url)
        download_mp3(url)
    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n⚠️  Download dibatalkan.")
        sys.exit(0)


if __name__ == "__main__":
    main()