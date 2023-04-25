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

resp = requests.get(url, headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})
soup = BeautifulSoup(resp.text, 'html.parser')
print(resp.status_code)
print('-'*20)

# 排除不必要的標籤
if soup.find_all('em'):
    for i in soup.find_all('em'):
        i.extract()
if soup.find('p', 'post-content__disclaimer'):
    for i in soup.find('p', 'post-content__disclaimer'):
        i.extract()
# 失敗
if soup.find('div', 'twitter-tweet twitter-tweet-rendered'):
    for i in soup.find('iframe', id='twitter-widget-0'):
        i.extract()
# content_box = ''
title = soup.find('h1', 'post__title').text
contents = soup.find('div', 'post-content').text
print(contents)

unedited = google_translate.translate_text(text = f'{title}\n\n{contents}')
result = replace_words.replacement_func(unedited)

path = f'/Users/jacobhuang/news/{month}/{title}.txt'
with open(path,'a') as file:
    file.writelines(f'{url}\n\n{title}\n\n{result}')