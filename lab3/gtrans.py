import os
from google.cloud import translate_v2 as translate
from translation_package.mod1 import TransLate, LangDetect, LanguageList

# Вставте шлях до вашого API ключа
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/premisterio/Documents/Файли/Інші файли/Google Translate API/empyrean-willow-435911-b7-388878703184.json"

# Ініціалізація Google Translate клієнта
translate_client = translate.Client()

# Перевірка функцій
print(TransLate("Hello, where are your from", "en", "uk"))
print(LangDetect("Hello, where are you from"))
LanguageList("screen", "Hello, where are you from")
