from deep_translator import GoogleTranslator
from langdetect import detect_langs


# Функція перекладу тексту
def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Error: {e}"


# Функція розпізнавання мови та впевненості визначення мови
def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected_langs = detect_langs(text)
        if set == "lang":
            return detected_langs[0].lang
        elif set == "confidence":
            return f"Confidence: {detected_langs[0].prob:.2f}"
        else:
            lang_conf_pairs = [f"Language: {lang.lang}, Confidence: {lang.prob:.2f}" for lang in detected_langs]
            return " | ".join(lang_conf_pairs)
    except Exception as e:
        return f"Error: {e}"


# Функція що повертає код мови або назву мови
def CodeLang(lang: str) -> str:
    lang_dict = {
        "en": "English", "uk": "Ukrainian", "de": "German", "fr": "French", "es": "Spanish"
    }
    try:
        # If input is a language code
        lang = lang.lower()
        if lang in lang_dict:
            return lang_dict[lang]

        # If input is a language name
        for code, name in lang_dict.items():
            if lang.capitalize() == name:
                return code

        return "Language not found"
    except Exception as e:
        return f"Error: {e}"

