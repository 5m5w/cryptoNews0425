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