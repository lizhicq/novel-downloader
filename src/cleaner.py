import re

def replace_novel_div(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    modified_content = clean_novel_txt(content)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(modified_content)

def clean_novel_txt(original_content: str) -> str:
    # 定义正则表达式模式，匹配多余的导航、广告等内容
    unwanted_phrases = [
        r"\（快捷键\s*←\）", r"\（快捷键\s*→\）",
        r"上一章", r"下一章", r"返回目录", r"加入书签", r"推荐本书",
        r"返回书页", r"返回顶部", r"我的藏书架", r"将本书加入书架",
        r"章节错误.*?举报", r"\|\s*", r"重要声明.*?小说.*?版权所有",
        r"飘天文学.*?小说阅读网", r"www\.piaotia\.com", r"Copyright.*"
    ]

    # 移除不需要的词句
    for pattern in unwanted_phrases:
        original_content = re.sub(pattern, "", original_content)

    # 清理多余的空行
    clean_text = re.sub(r"\n\s*\n", "\n", original_content).strip()
    
    return clean_text

    
if __name__ == '__main__':
    replace_novel_div('data/novels/妖武乱世.txt')
    
        