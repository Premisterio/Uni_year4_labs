import os
from google.cloud import translate_v2 as translate

# Посилання на мій API ключ
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/premisterio/Documents/Файли/Інші файли/Google Translate API/empyrean-willow-435911-b7-388878703184.json"

# Ініціалізація клієнта
translate_client = translate.Client()


# Функція перекладу
def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        if scr == dest:
            return text
        if scr == 'auto':
            detection = translate_client.detect_language(text)
            scr = detection['language']
        result = translate_client.translate(text, source_language=scr, target_language=dest)
        return result['translatedText']
    except Exception as e:
        return f"Error: {e}"


# Функція розпізнавання мови
def LangDetect(text: str, set: str = "all") -> str:
    try:
        result = translate_client.detect_language(text)
        if set == "lang":
            return result['language']
        elif set == "confidence":
            return str(result['confidence'])
        else:
            return f"Language: {result['language']}, Confidence: {result['confidence']}"
    except Exception as e:
        return f"Error: {e}"


# Функція що повертає код мови
def CodeLang(lang: str) -> str:
    lang_dict = {
        "en": "English", "uk": "Ukrainian", "de": "German", "fr": "French", "es": "Spanish"
    }
    try:
        if lang in lang_dict:
            return lang_dict[lang]
        else:
            for code, name in lang_dict.items():
                if lang.capitalize() == name:
                    return code
        return "Language not found"
    except Exception as e:
        return f"Error: {e}"


# Функція що виводить всі мови, доступні клієнту API
def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        supported_langs = translate_client.get_languages()
        if out == "screen":
            print(f"{'N':<5}{'Language':<20}{'ISO-639 code':<10}{'Text':<20}")
            print("-" * 55)
            for i, lang in enumerate(supported_langs[:20], 1):
                if text:
                    translated_text = TransLate(text, 'auto', lang['language'])
                else:
                    translated_text = ""
                print(f"{i:<5}{lang['name']:<20}{lang['language']:<10}{translated_text:<20}")
        return "Ok"
    except Exception as e:
        return f"Error: {e}"
