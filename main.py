from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import yt_dlp
import os
import tempfile

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
        "outtmpl": os.path.join(temp_dir, "%(title)s.%(ext)s"),  # avoid downloads/
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filepath = ydl.prepare_filename(info)


    if not os.path.exists(filepath):
        raise HTTPException(status_code=500, detail="Download failed. File not found.")

  
    return FileResponse(
        filepath,
        media_type="audio/mp4",
        filename=os.path.basename(filepath)
    )
