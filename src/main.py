from downloader import download_novel,save_chapters_to_text
from parser import * # type: ignore
import os

def main():
    url = "https://www.piaotia.com/html/15/15296/"
    chapters = get_novel_chapters(url)
    chapters = download_novel(chapters)
    chapters[:10]
    save_chapters_to_text(
        chapters,     
        os.path.join(
            os.getcwd(),
            'data/novels/妖武乱世.txt'
    ))

if __name__ == "__main__":
    main()
