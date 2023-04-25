from bs4 import BeautifulSoup
import requests
from datetime import datetime
import replace_words
import google_translate

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.5",
           "Pragma": "no-cache",
           "Cache-Control": "no-cache"}

cookies = {'muid': 'LY3EGO86Xdlr9TN'}
#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####
url = input("news url: ")
#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####
resp = requests.get(url, headers = headers, cookies=cookies)
soup = BeautifulSoup(resp.content, 'html.parser')
print(resp.status_code)

now = datetime.now()
year = now.year
month = now.month
day = now.day

content_box=''
title = soup.find('h1', 'm-detail-header--title').get_text()
print(title)
contents = soup.find('div', 'm-detail--body')
for i in contents.find_all('p'):
    content_box = content_box + i.get_text()
print(content_box)

#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####
#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####
unedited = google_translate.translate_text(text = f'{title}\n\n{content_box}')
result = replace_words.replacement_func(unedited)
path = f'/Users/jacobhuang/news/{month}/{title}.txt'
with open(path,'a') as file:
    file.writelines(f'{url}\n\n{title}\n\n{result}')

#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####
#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####