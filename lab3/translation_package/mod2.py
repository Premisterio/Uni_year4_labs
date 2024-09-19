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
