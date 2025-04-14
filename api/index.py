import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse
from module.youtube import start_youtube_download_asynchronously
import logging 

load_dotenv()
COMMON_PHRASE = os.environ["COMMON_PHRASE"]

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


@app.get("/")
async def root():
    logger.debug("Hello World")
    return [{"hello":"world"}]

@app.post("/download_video")
async def download_video(request: Request, url: str):
    auth_header = request.headers.get("Authorization")

    if auth_header != f"Bearer {COMMON_PHRASE}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    data = await request.json()
    if "videoURL" not in data:
        raise HTTPException(status_code=400, detail="Bad Request: 'videoURL' is required")
    video_url = data["videoURL"]

    # Download YouTube Video
    try:
        download_status = await start_youtube_download_asynchronously(video_url)
        if download_status:
            # return Response(status_code = 200)
            return
        else:
            raise HTTPException(status_code=500, detail=f"Download Error: {download_status}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# ./tmp_video/afewmomentslater.mp4
@app.get("/tmp_video/{file_name}")
async def download_file(file_name: str):
    file_path = f"tmp_video/{file_name}"
    return FileResponse(path=file_path, filename=file_name, media_type='application/octet-stream')
