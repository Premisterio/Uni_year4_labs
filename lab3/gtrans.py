from translation_package.mod1 import TransLate, LangDetect, LanguageList

# Перевірка функцій
print(TransLate("Hello, where are your from", "en", "uk"))
print(LangDetect("Hello, where are you from"))
LanguageList("screen", "Hello, where are you from")
