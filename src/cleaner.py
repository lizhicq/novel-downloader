def replace_html_div(html_content):
    html_content = html_content.replace('    ', '  \n')
    html_content = html_content.replace('必应~搜*\:择.日。网~,`全，网，最快。  ', '')
    return html_content

def replace_novel_div(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    modified_content = replace_html_div(content)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(modified_content)
        
        
if __name__ == '__main__':
    replace_novel_div('data/novels/妖武乱世.txt')
        