from ebooklib import epub
import os,re

def extract_number(filename):
    # 使用正则表达式从文件名中提取章节数字
    match = re.search(r'第(\d+)章', filename)
    if match:
        return int(match.group(1))
    return 0


def create_epub(folder_path, output_file):
    # 创建EPUB书籍对象
    book = epub.EpubBook()

    # 设置书籍的标识符、标题和语言
    book.set_identifier('文抄公-妖武乱世')
    book.set_title('妖武乱世')
    book.set_language('zh')
    book.add_author("文抄公")

    # 添加封面
    # book.set_cover("image.jpg", open("path_to_cover_image.jpg", "rb").read())

    # 读取文件夹中的所有txt文件并添加为章节
    
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    files.sort(key=extract_number)  # 对文件名进行字母顺序排序
    print(files)
    
    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            chapter_title = os.path.splitext(file_name)[0]

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 创建章节
            chapter = epub.EpubHtml(title=chapter_title, file_name=chapter_title + '.xhtml', lang='zh')
            chapter.content = '<h1>{}</h1><p>{}</p>'.format(chapter_title, content)
            book.add_item(chapter)

            # 添加章节到目录
            book.toc = (
                epub.Link(chapter_title + '.xhtml', chapter_title, chapter_title),
                (epub.Section("Simple book"), (chapter,)),
            )
            break

    # 添加标准导航文件和NCX文件
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # 写入EPUB文件
    epub.write_epub(output_file, book, {})

    print("EPUB文件已创建：{}".format(output_file))

if __name__ == "__main__":
    folder_path = "/Users/lizhicq/GitHub/novel-downloader/data/novels/test"
    epub_path = "/Users/lizhicq/GitHub/novel-downloader/data/novels/文抄公-妖武乱世.epub"
    create_epub(folder_path, epub_path) 
