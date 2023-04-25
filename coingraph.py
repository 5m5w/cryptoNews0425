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
if soup.find(class_='inlineBanner'):
  for i in soup.find_all(class_='inlineBanner'):
    i.extract()
if soup.find('em'):
  for i in soup.find_all('em'):
    i.extract()

title = soup.find(class_='tdb-title-text').get_text()
print(title)
p = soup.find(class_='td_block_wrap tdb_single_content tdi_86 td-pb-border-top td_block_template_1 td-post-content tagdiv-type').get_text()
print(p)

unedited = google_translate.translate_text(text = f'{title}\n{p}')
result = replace_words.replacement_func(unedited)

path = f'/Users/jacobhuang/news/{month}/{title}.txt'
with open(path,'a') as file:
    file.writelines(f'{url}\n\n{title}\n\n{result}')