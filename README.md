# YouTube to M4A Downloader

A simple FastAPI web app that allows users to paste a YouTube video URL and download the audio in `.m4a` format — without needing to install FFmpeg.

---

## Features

- Paste any YouTube URL to download the best quality audio
- Automatically downloads `.m4a` format (no FFmpeg required)
- No need to install external YouTube downloader software
- Clean frontend with HTML and CSS
- FastAPI backend powered by `yt-dlp`

---

## Requirements

- Python 3.8 or higher
- `yt-dlp`
- `fastapi`
- `uvicorn`

---

## Installation

```bash
git clone https://github.com/Thirdsantos/Youtube-to-M4A.git
cd youtube-m4a-downloader
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
