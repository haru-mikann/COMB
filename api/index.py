from fastapi import FastAPI
from fastapi.responses import FileResponse
import logging 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


@app.get("/")
async def root():
    logger.debug("Hello World")
    return [{"hello":"world"}]

# ./tmp_video/afewmomentslater.mp4
@app.get("/tmp_video/{file_name}")
async def download_file(file_name: str):
    file_path = f"tmp_video/{file_name}"
    return FileResponse(path=file_path, filename=file_name, media_type='application/octet-stream')
