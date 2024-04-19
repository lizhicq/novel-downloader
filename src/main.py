from downloader import download_novel,save_chapters_to_text
from parser import * # type: ignore
from utils import *
import os

def main():
    url = "https://www.piaotia.com/html/15/15296/"
    chapters = get_novel_chapters(url)
    chapters = download_novel(chapters)
    novel = 'data/novels/妖武乱世.txt'
    save_chapters_to_text(
        chapters,     
        os.path.join(
            os.getcwd(),
            novel
    ))
    replace_novel_div(novel)

if __name__ == "__main__":
    main()
