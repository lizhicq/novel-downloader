from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def get_html_from_url(url):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
    chrome_options.binary_location = (
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    )

    # Initialize a Chrome webdriver
    driver = webdriver.Chrome(
        executable_path='~/Applications/Drivers/chromedriver', 
        options=chrome_options
    )
    # Load the page
    driver.get(url)

    # Get the source HTML of the page
    html = driver.page_source

    # Close the browser
    driver.quit()

    return html

def get_novel_chapters(content_url:str):
    # Replace 'html_content' with your actual HTML content string
    html_content = get_html_from_url(content_url)

    # Using BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Finding all <a> tags within <li> tags
    chapter_list = soup.find_all('li')

    # Extracting chapter names and URLs
    chapters = []
    for chapter in chapter_list:
        link = chapter.find('a')
        if link and 'href' in link.attrs:
            chapter_url = content_url + "/" + link['href'].strip()
            chapter_info = {
                'title': link.text.strip() or "bad chapter", 
                'url': chapter_url,
                'content':""
            }
            chapters.append(chapter_info)
    return chapters


def extract_novel_chapter(chapter_url):
    chapter_html = get_html_from_url(chapter_url)
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(chapter_html, 'html.parser')
    
    # 寻找包含小说内容的标签
    content_div = soup.find('div', id='content')
    # 移除不需要的子元素，如链接等
    for element in content_div.find_all(['a', 'script', 'table', 'div']):
        element.decompose()

    # 打印清理后的文本
    clean_text = content_div.get_text()
    return clean_text
