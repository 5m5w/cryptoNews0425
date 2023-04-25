from bs4 import BeautifulSoup
import requests
from google.cloud import translate

result =''
def translate_text(text="", project_id="able-hull-381502"):
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": "zh-TW",
        }
    )
    for translation in response.translations:
        result = "Translated text: {}".format(translation.translated_text)
    return result

url = 'https://www.bankless.com/where-does-ethereum-go-next'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
print(resp.status_code)

title = soup.find(calss_='wow fadeInUp')
print(title)
summary = soup.find(class_='desc wow fadeInUp')
print(summary)
contents = soup.find(class_='contents').get_text()
print(contents)

result = translate_text(text = f'{title}\n{summary}\n{contents}')
print(result)