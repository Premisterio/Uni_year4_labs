from translation_package.mod2 import TransLate, LangDetect

# Перевірка функцій другого модуля
# Викорисатння функції TransLate()
print(TransLate("Hello, what is the current situation on the frontline", "en", "uk"))
# Використання функції LangDetect() для визначення мови
print(LangDetect("Hello, what is the current situation on the frontline"))

