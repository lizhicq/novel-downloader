from downloader import download_novel,save_chapters_to_text
from parser import * # type: ignore
from cleaner import *
import os,time

def main():
    url = "https://www.piaotia.com/html/8/8791/"
    novel = 'iCloud/Novel/文抄公-逍遥梦路.txt'
    
    max_retry = 5
    delay = 5
    for attempt in range(max_retry):
        try:
            chapters = get_novel_chapters(url)
            chapters = download_novel(chapters)
            break
        except Exception as e:
            if "ERR_CONNECTION_CLOSED" in str(e):
                print(f"Attempt {attempt + 1} failed with connection closed error. Retrying in {delay} seconds...")
                time.sleep(delay)  # Wait before retrying
            else:
                print("An unexpected error occurred:", e)
                break  # Exit retry loop if a different error occurs
    novel_path = os.path.join(os.getenv('HOME'), novel)
    save_chapters_to_text(chapters,novel_path)
    replace_novel_div(novel_path)

if __name__ == "__main__":
    main()
