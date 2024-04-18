from downloader import download_novel,save_chapters_to_text
from parser import * # type: ignore

def main():
    url = "https://www.piaotia.com/html/14/14836/"
    chapters = get_novel_chapters(url)
    chapters = download_novel(chapters)
    save_chapters_to_text(chapters, '~/GitHub/novel-downloader/data/novels/灵境行者.txt')

if __name__ == "__main__":
    main()
