import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
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

@app.get("/vid_url")
async def get_vid_url(request: Request):
    auth_header = request.headers.get("Authorization")

    if auth_header != f"Bearer {COMMON_PHRASE}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    data = await request.json()
    if "videoURL" not in data:
        raise HTTPException(status_code=400, detail="Bad Request: 'videoURL' is required")
    video_url = data["videoURL"]

    Return Responce(status_code = 204)

# ./tmp_video/afewmomentslater.mp4
@app.get("/tmp_video/{file_name}")
async def download_file(file_name: str):
    file_path = f"tmp_video/{file_name}"
    return FileResponse(path=file_path, filename=file_name, media_type='application/octet-stream')
