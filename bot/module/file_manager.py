import os
from datetime import datetime

# =======================================================
# GetLastModifyDate()
# ファイルの最終更新日時を取得
#
# isPassed24hours()
# ファイルの最終更新日時を指定のフォーマット(GetLastModifyDate()のReturn形式)でとり、24時間以上経過したかどうかを論理型で返す
#
# GetDirectorySize()
# 指定のディレクトリのサイズを取得(MegaBytes単位でReturn)
#
# Delete()
# 指定のファイルを消去
# =======================================================

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
    mod_time_readable = datetime.fromtimestamp(date_last_modified).strftime('%Y-%m-%d-%H-%M-%S')
    # =========================
    # Return format : YEAR-MONTH-DATE-HOUR-MINUTE-SECOND
    # e.g.
    # 2024-09-01-03-41-09
    # =========================
    return mod_time_readable

# EN: Check if 24 hours has passed from the last modify
# JP: ファイルの最終更新日時から24時間以上経過しているかを判断
# Return True when passed 24 hours, return False when not pass 24 hours
def isPassed24hours(date_string: str) -> bool:
    """
    input   : date format (last modify date)
    output  : bool
    """
    try:
        # Convert the input string to a datetime object
        date_format = "%Y-%m-%d-%H-%M-%S"
        given_time = datetime.strptime(date_string, date_format)

        # Get the current time
        current_time = datetime.now()

        # Check if the difference is more than 24 hours
        return current_time - given_time > timedelta(hours=24)
    except ValueError:
        raise ValueError("The date string must be in the format 'YYYY-MM-DD-HH-MM-SS'")

def isPassed24hoursByPath(file_path) -> bool:
    """
    input   : string (filepath)
    output  : bool
    """
    try:
        # file path to date format 
        last_modify_date = GetLastModifyDate(file_path)

        # Convert the input string to a datetime object
        date_format = "%Y-%m-%d-%H-%M-%S"
        given_time = datetime.strptime(date_string, date_format)

        # Get the current time
        current_time = datetime.now()

        # Check if the difference is more than 24 hours
        return current_time - given_time > timedelta(hours=24)
    except ValueError:
        raise ValueError("The date string must be in the format 'YYYY-MM-DD-HH-MM-SS'")

# EN: Check tmp directory size
# JP: ディレクトリのサイズを取得
def GetDirectorySize(filepath):
    full_filepath = filepath # TODO tmpディレクトリ作成後（パス決定後）に再度設定

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(full_filepath):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # シンボリックリンクでないファイルのみサイズを取得
            if not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)
    size_in_megabytes = total_size / (1024 * 1024) # Convert to MB
    # =========================
    # Return format : MegaBytes
    # e.g.
    # 25.23689
    # =========================
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
