import os
import glob
import file_manager
from dotenv import load_dotenv
load_dotenv()

# 指定するディレクトリ
target_dir = os.getenv()

def StorageManager():
    mp4_files = glob.glob(os.path.join(target_dir, "**", "*.mp4"), recursive=True)
    for file_path in mp4_files:
        # print(f"Processing: {file_path}")  # ここに処理を追加
        ifDelete = file_manager file_manager.isPassed24hours(file_path)
        if ifDelete == True:
            file_manager.Delete(file_path)

if __name__ == "__main__":
    print("main")
