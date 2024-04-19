from bs4 import BeautifulSoup
from parser import * # type: ignore
from multiprocessing import Pool, Manager


def download_chapter(chapter):
    try:
        url = chapter['url']
        content = extract_novel_chapter(url)
        #print('successfully download',chapter['title'])
        return {'title': chapter['title'], 'url': url, 'content': content}
    except Exception as e:
        #print('error message', chapter['title'], e)
        return {'title': chapter['title'], 'url': url, 'content': ""}
    

def download_novel(chapters:list):
    # manager = Manager()
    # chapters = manager.list(chapters)
    unfinished_chaps = [chap for chap in chapters if chap['content'] == ""]  
    while len(unfinished_chaps) > 0:
        print('unfinished', len(unfinished_chaps), 'total', len(chapters))
        with Pool(processes=8) as pool:
            results = pool.map(download_chapter, unfinished_chaps)
        for result in results:
            for chap in chapters:
                if chap['title'] == result['title']:
                    chap['content'] = result['content']
        unfinished_chaps = [chap for chap in chapters if chap['content'] == ""]
    return list(chapters)

def save_chapters_to_text(chapters, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for chapter in chapters:
            if chapter:
                file.write(f"{chapter['content']}\n")
                file.write("\n\n")  # Add extra newlines for readability between chapters
