from downloader import download_novel,save_chapters_to_text
from epub_creator import create_novel_epub
from parser import * # type: ignore
from cleaner import *
import os,time

def main():
    url = "https://www.piaotia.com/html/15/15296/"
    save_path = 'GitHub/novel-downloader/data/novels/'
    author = '文抄公'
    book = '妖武乱世'
    
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
    
    save_path = os.path.join(os.getenv('HOME'), save_path, author + '-' + book)
    
    save_chapters_to_text(chapters,save_path)
    # create_novel_epub(author, book, chapters, save_path)
    
    
if __name__ == "__main__":
    main()
