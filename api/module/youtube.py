import os
from dotenv import load_dotenv
from yt_dlp import YoutubeDL
import logging
import asyncio

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

load_dotenv()

def start_youtube_download(url):
    path = os.environ["YOUTUBE_PATH"]
    try:
        logger.info("start youtube download")
        option = {
            "outtmpl":f"{path}%(title)s.%(ext)s"
        }#パスは実行する環境に合わせて
        with YoutubeDL(option) as ydl:
            ydl.download(url)
        return True
    except Exception as e:
        return e

async def start_youtube_download_asynchronously(url):
    return await asyncio.to_thread(start_youtube_download, url)

def delete_file(path):
    try:
        os.remove(path)
    except Exception as e:
        logger.info(f"delete file error -> {e}")
