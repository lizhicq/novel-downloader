from parser import * # type: ignore
from process_tracker import print_progress_bar
from multiprocessing import Pool, Manager
from cleaner import clean_novel_txt

def download_chapter(chapter):
    try:
        url, title = chapter['url'], chapter['title']
        content = extract_novel_chapter(url)
        content = content.replace(title, '') # Clean addition title in content
        content = clean_novel_txt(content)
        output_file = os.path.join("/Users/lizhicq/GitHub/novel-downloader/data/test/", f'{title}.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f'{content}')
        return {'title': chapter['title'], 'url': url, 'content': content}
    except Exception as e:
        print('error message', chapter['title'], e)
        return {'title': chapter['title'], 'url': url, 'content': ""}
    

def download_novel(chapters:list):
    return main_process(chapters)

def save_chapters_to_text(chapters, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for chapter in chapters:
            if chapter:
                file.write(f"{chapter['title']}\n")
                file.write(f"{chapter['content']}\n")
                file.write("\n\n")  # Add extra newlines for readability between chapters


def task(chapter, progress_counter, lock, total_tasks):
    """
    Sub task that downloads the chapter online
    """
    chapter = download_chapter(chapter)
    with lock:
        progress_counter.value += 1
        print_progress_bar(progress_counter.value/total_tasks)
    return chapter
    
def main_process(chapters:list):
    unfinished_chaps = [chap for chap in chapters if chap['content'] == ""]
    counter = 0  
    while len(unfinished_chaps) > 0:
        counter += 1
        manager = Manager()
        progress_counter = manager.Value('i', 0) # Shared integer
        lock = manager.Lock()
        print('\nunfinished', len(unfinished_chaps), 'total', len(chapters))
        tasks = [(chap, progress_counter, lock, len(unfinished_chaps)) 
                    for chap in unfinished_chaps]
        
        with Pool() as pool:
            results_async = pool.starmap_async(task, tasks)
            results = results_async.get()

        for result in results:
            for chap in chapters:
                if chap['title'] == result['title']:
                    chap['content'] = result['content']
        unfinished_chaps = [chap for chap in chapters if chap['content'] == ""]
        print_progress_bar(1 - len(unfinished_chaps) / len(chapters))
        if counter > 10:
            break
        
    return list(chapters)