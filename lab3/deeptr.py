from translation_package.mod2 import TransLate, LangDetect, CodeLang

# Використання функції TransLate()
translated_text = TransLate("Hello, what is the current situation on the frontline", "en", "uk")
print(translated_text)

# Використання функції LangDetect() для визначення мови
detected_language_info = LangDetect("Hello, what is the current situation on the frontline")
print(detected_language_info)

# Отримання коду мови з інформації про мову
detected_language = LangDetect("Hello, what is the current situation on the frontline", set="lang")
language_code = CodeLang(detected_language)
print(language_code)
