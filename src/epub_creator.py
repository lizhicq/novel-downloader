from ebooklib import epub
import os


def create_novel_epub(author_name: str, book_name: str, chapters: list, save_path):
    book = epub.EpubBook()
    identifier = author_name + '-' + book_name
    book.set_identifier(identifier)
    book.set_language('ch')
    book.set_title(book_name)
    book.add_author(author_name)
    
    # Add each chapter to the EPUB
    for index, chapter in enumerate(chapters, start=1):
        if chapter:
            formatted_content = chapter["content"].replace("\n", "<br/>")
            # Create a chapter in HTML format
            c1 = epub.EpubHtml(title=chapter['title'], file_name=f'chap_{index}.xhtml', lang='en')
            c1.content = f'<h1>{chapter["title"]}</h1><p>{formatted_content}</p>'

            # Add chapter to the book
            book.add_item(c1)
            book.spine.append(c1)

    # Define EPUB Table Of Contents and the book spine (order of book content)
    book.toc = (epub.Link(f'chap_{i}.xhtml', chapters[i-1]['title'], f'chap_{i}') for i in range(1, len(chapters) + 1))
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Write the EPUB file
    epub_path = save_path
    epub.write_epub(epub_path, book, {})

# Replace 'content.txt' and 'output.epub' with your file paths
if __name__ == "__main__":
    pass
