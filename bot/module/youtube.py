import os
from dotenv import load_dotenv
from yt_dlp import YoutubeDL
import datetime
import logging
import requests


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

load_dotenv()


def start_youtube_download(url):
    path = os.environ["YOUTUBE_PATH"]
    logger.info("path => " + path)
    try:
        created_at = datetime.datetime.now()
        file_name = created_at.strftime("%Y%m%d%H%M%S")
        logger.info("start youtube download")
        option = {
            "outtmpl":f"{path}/{file_name}.%(ext)s",
            'format':'bestvideo[ext=mp4]+bestaudio/best[ext=mp4]',
            "merge_output_format": "mp4",  # 出力形式をmp4に指定
            "quiet": False,  # 詳細な情報を表示
            "noplaylist": True  # プレイリストを無効化
        }#パスは実行する環境に合わせて
        ydl = YoutubeDL(option)
        ydl.download(url)
        # TODO webダウンロードリンクを発行
        
        link = f"http://{get_gip_addr()}:36512/{path.split("/")[-1]}/{file_name}.mp4"
        return "Done!\n" + link
    except Exception as e:
        logger.info(f"youtube download error  -> {e}")
        return f"youtube download error  -> {e}"
    

def delete_file(path):
    try:
        os.remove(path)
    except Exception as e:
        logger.info(f"delete file error -> {e}")

def get_gip_addr():
    #server の global IP Address を return
    res = requests.get("http://ipaddr.show")
    return res.text.rstrip("\n")
    