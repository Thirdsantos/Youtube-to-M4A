from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import yt_dlp
import os
import tempfile
from yt_dlp.utils import DownloadError


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/download")
def download(url: str):
    temp_dir = tempfile.gettempdir()

    ydl_opts = {
        "format": "bestaudio[ext=m4a]/bestaudio/best",
        "outtmpl": os.path.join(temp_dir, "%(title)s.%(ext)s"),
        "quiet": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filepath = ydl.prepare_filename(info)

    except DownloadError as e:

        raise HTTPException(
            status_code=400,
            detail="Failed to download the video. It might be private, unavailable, or blocked."
        )

    except Exception as e:
   
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )

    if not os.path.exists(filepath):
        raise HTTPException(
            status_code=500,
            detail="Download failed. File not found on server."
        )

    return FileResponse(
        filepath,
        media_type="audio/mp4",
        filename=os.path.basename(filepath)
    )