from downloader import download_novel,save_chapters_to_text
from parser import * # type: ignore
from cleaner import *
import os,time

def main():
    url = "https://www.piaotia.com/html/14/14060/"
    novel = 'data/novels/文抄公-神秘之劫.txt'
    
    max_retry = 5
    delay = 5
    for attempt in max_retry:
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

    save_chapters_to_text(
        chapters,     
        os.path.join(
            os.getcwd(),
            novel
    ))
    replace_novel_div(novel)

if __name__ == "__main__":
    main()
