from bs4 import BeautifulSoup
import requests
from datetime import datetime
import replace_words
import google_translate

now = datetime.now()
year = now.year
month = now.month
day = now.day

url = input('crypto news: ')
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
if resp.status_code != 200:
    print('error')
    
content_box = ''
title = soup.find('h1', 'typography__StyledTypography-owin6q-0 kVbxLR').text
summary = soup.find('h2', 'typography__StyledTypography-owin6q-0 cysoWk').text
contents = soup.find_all('div', 'common-textstyles__StyledWrapper-sc-18pd49k-0 eSbCkN')
for i in contents:
    content = i.find('div', 'typography__StyledTypography-owin6q-0 bYmaON at-text').text
    if 'Read more:' in content: 
        content = content.split('Read more:')[0]
    elif 'UPDATE (' in content:
        content = content.split('UPDATE (')[0]
    elif 'Read the full story here:' in content:
        content = content.split('Read the full story')[0]
    else:
        pass
    content_box += content
print(content_box)

unedited = google_translate.translate_text(text = f'{title}\n{summary}\n{content_box}')
result = replace_words.replacement_func(unedited)

path = f'/Users/jacobhuang/news/{month}/{title}.txt'
with open(path,'a') as file:
    file.writelines(f'{url}\n\n{title}\n{summary}\n{result}')