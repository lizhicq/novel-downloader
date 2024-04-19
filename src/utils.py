def replace_html_div(html_content):
    return html_content.replace('    ', '  \n')

def replace_novel_div(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    modified_content = replace_html_div(content)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(modified_content)
        
        
if __name__ == '__main__':
    replace_novel_div('data/novels/灵境行者.txt')
        