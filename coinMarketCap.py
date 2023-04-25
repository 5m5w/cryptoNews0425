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
print(resp.status_code)
print('-'*20)

# 排除不必要的內容
if soup.find_all('div', 'disclaimer'):
    for i in soup.find_all('div', 'disclaimer'):
        i.extract()
if soup.find_all(class_='sc-bdfBwQ iumvLK'):
    for i in soup.find_all(class_='sc-bdfBwQ iumvLK'):
        i.extract()
if soup.find_all('em'):
    for i in soup.find_all('em'):
        i.extract()

title = soup.find('h1', 'sc-bdfBwQ Text-msjfkz-0 Heading-juwhnu-0 hoXOTC dAnDNe')
title = title.text
print(title)
summary = soup.find('div', 'sc-bdfBwQ ArticleContent__ArticleSummaryBox-sc-18n1x4l-1 ihJtHv dwcfaP')
summary = summary.text
print(summary)
article = soup.find('article', 'sc-bdfBwQ Container-sc-4c5vqs-0 ArticleContent__ArticleContainer-sc-18n1x4l-0 cdVqKV khdEkh ljODsN')
article = article.text
print(article)
print('-'*20)

unedited = google_translate.translate_text(text = f'{title}\n{summary}\n{article}')
result = replace_words.replacement_func(unedited)

path = f'/Users/jacobhuang/news/{month}/{title}.txt'
with open(path,'a') as file:
    file.writelines(f'{url}\n\n{title}\n\n{result}')
