import os
from datetime import datetime

class FileInfo:
    # def __init__(self, name, path, date):
    def __init__(self, path):
        # self.filename = filename
        self.filepath = path
        # self.date = date

# EN: Check file last modify date
# JP: ファイルの最終更新日時を取得
def GetLastModifyDate(filepath):
    full_filepath = filepath # TODO tmpディレクトリ作成後（パス決定後）に再度設定
    date_last_modified = os.path.getmtime(full_filepath)
    mod_time_readable = datetime.fromtimestamp(date_last_modified).strftime('%Y-%m-%d-%H-%M-%S') # Format: 2024-07-06 04:19:21

    # Return format : YEAR-MONTH-DATE HOUR:MINUTE:SECOND
    # e.g.
    # 2024-09-01-03-41-09

    return mod_time_readable

# EN: Check file duration (How long to reach 24 hours from latest change)
# JP: ファイルの期限を確認（最終更新日時から24時間まであとどれくらいか）
# def File_duration():
#     return duration

# EN: Check tmp directory size
# JP: ディレクトリのサイズを取得
def Directory_size(filepath):
    full_filepath = filepath # TODO tmpディレクトリ作成後（パス決定後）に再度設定

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(full_filepath):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # シンボリックリンクでないファイルのみサイズを取得
            if not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)
    size_in_megabytes = total_size / (1024 * 1024) # Convert to MB

    # Return format : MegaBytes
    # e.g.
    # 25.23689

    return size_in_megabytes

# Delete file
def Delete(filepath):
    full_filepath = filepath # TODO tmpディレクトリ作成後（パス決定後）に再度設定

    if os.path.isfile(filepath): # Check if file exists
        os.remove(filepath)
        print(f"Deleted {filepath} successfully!")
    else:
        print(f"Delete failed. File {filepath} does not exist.")

if __name__ == "__main__":
	print("main")
