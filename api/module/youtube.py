import os
from dotenv import load_dotenv
from yt_dlp import YoutubeDL
import logging

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
        ydl = YoutubeDL(option)
        ydl.download(url)
        # TODO webダウンロードリンクを発行
        return "download Success"
    except Exception as e:
        logger.info(f"youtube download error  -> {e}")
        return f"download fail. \n{e}"
    

def delete_file(path):
    try:
        os.remove(path)
    except Exception as e:
        logger.info(f"delete file error -> {e}")
