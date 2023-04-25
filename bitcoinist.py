from bs4 import BeautifulSoup
import requests
from datetime import datetime
import replace_words
import google_translate

now = datetime.now()
year = now.year
month = now.month
day = now.day

url = input("crypto news: ")
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
print(resp.status_code)

# 排除不必要的標籤
if soup.find_all('div', 'jeg_ad jeg_ad_article jnews_content_inline_2_ads'):
    for i in soup.find_all('div', 'jeg_ad jeg_ad_article jnews_content_inline_2_ads'):
        i.extract()
if soup.find('div', 'svecc-text-banner svecc-text-banner--punt'):
    for i in soup.find_all('div', 'svecc-text-banner svecc-text-banner--punt'):
        i.extract()
if soup.find_all('div', 'related-reading-shortcode'):
    for i in soup.find_all('div', 'related-reading-shortcode'):
        i.extract()
if soup.find_all('div', 'svecc-text-banner svecc-text-banner--mbit'):
    for i in soup.find_all('div', 'svecc-text-banner svecc-text-banner--mbit'):
        i.extract()
if soup.find_all('pre', style_='text-align: center; position: relative;'):
    for i in soup.find_all('pre', style_='text-align: center; position: relative;'):
        i.extract()
if soup.find_all('div', 'disclaimer-shortcode'):
    for i in soup.find_all('div', 'disclaimer-shortcode'):
        i.extract()


content_box=''
title = soup.find('h1', 'jeg_post_title').get_text()
contents = soup.find('div', 'content-inner')
for i in contents.find_all('p'):
    content_box = content_box + i.get_text()
print(content_box)  

# unedited = google_translate.translate_text(text = f'{title}\n\n{content_box}')
# result = replace_words.replacement_func(unedited)

# path = f'/Users/jacobhuang/news/{month}/{title}.txt'
# with open(path,'a') as file:
#     file.writelines(f'{url}\n\n{title}\n\n{result}')
