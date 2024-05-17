from downloader import download_novel
from parser import * # type: ignore
from cleaner import *
from utils.epub_maker import create_epub_from_multiple_txts
import time

def main():
    url = "https://www.piaotia.com/html/10/10141/"
    author = '文抄公'
    book = '超凡黎明'
    
    max_retry = 5
    delay = 5
    for attempt in range(max_retry):
        try:
            chapters = get_novel_chapters(url)
            chapters = download_novel(chapters, book)
            break
        except Exception as e:
            if "ERR_CONNECTION_CLOSED" in str(e):
                print(f"Attempt {attempt + 1} failed with connection closed error. Retrying in {delay} seconds...")
                time.sleep(delay)  # Wait before retrying
            else:
                print("An unexpected error occurred:", e)
                break  # Exit retry loop if a different error occurs
    
    # save_chapters_to_text(chapters,save_path)
    create_epub_from_multiple_txts(author,book)
    
    
if __name__ == "__main__":
    main()
