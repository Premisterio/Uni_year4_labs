from google.cloud import translate_v2 as translate
import os

# Set the path to your Google credentials file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/premisterio/Documents/Файли/Інші файли/Google Translate API/empyrean-willow-435911-b7-388878703184.json"

# Initialize the Google Translator
translate_client = translate.Client()

# Language dictionary
lang_dictionary = {
    "English": "en",
    "Ukrainian": "uk",
    "German": "de",
    "French": "fr",
    "Spanish": "es",
    "Chinese": "zh",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko"
}

# Translate function using google-cloud-translate
def translate_text(text, lang_code):
    try:
        result = translate_client.translate(text, target_language=lang_code)
        return result['translatedText']
    except Exception as e:
        print(f"Error in translation: {e}")
        return None

# Language detection function
def detect_language(text):
    try:
        result = translate_client.detect_language(text)
        return result['language'], result['confidence']
    except Exception as e:
        print(f"Error in language detection: {e}")
        return None, None

# Convert language name to code and vice versa
def code_lang(lang):
    if lang.capitalize() in lang_dictionary:
        return lang_dictionary[lang.capitalize()]
    elif lang in lang_dictionary.values():
        for name, code in lang_dictionary.items():
            if code == lang:
                return name
    else:
        raise ValueError("Language not found in dictionary")

# Main loop for user input
while True:
    try:
        text_to_translate = input("Enter text to translate: ").lower().strip()

        # Display available languages
        for lang, code in lang_dictionary.items():
            print(f"{lang}: {code}")

        # Ask user for the target language
        target_language = input("Enter the language you want to translate to: ").strip().capitalize()

        if target_language in lang_dictionary:
            target_language_code = code_lang(target_language)
            break
        elif target_language in lang_dictionary.values():
            target_language_code = target_language
            break
        else:
            raise ValueError("Invalid language code. Please try again.")
    except ValueError as ve:
        print(ve)

# Perform translation
translated_text = translate_text(text_to_translate, target_language_code)
print(f"Translated text: {translated_text}")

# Detect the language of the input text
detected_lang, confidence = detect_language(text_to_translate)
if detected_lang:
    print(f"Detected language: {detected_lang} with confidence: {confidence}")

# Show full name or code of the chosen language
print("Full name or code: ", code_lang(target_language_code))
