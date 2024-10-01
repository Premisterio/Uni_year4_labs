# Використовуємо regular expressions
import re


# Сортування укр мова незалежно від реєстру, потім англійська мова незалежно від реєстру
def custom_sort_key(word):
    first_char = word[0].lower()
    if first_char in ukrainian_words:
        return 0, word.lower()
    else:
        return 1, word.lower()


try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        # За допомогою regular expression шукаємо речення, виділяючи розділові знаки
        match = re.search(r'([^.?!]*[.?!])', text)
        if match:
            first_sentence = match.group(0).strip()
            print("Перше речення:", first_sentence)
        else:
            print("Речення не знайдено.")

        words = re.findall(r'\b\w+\b', text)  # Пошук слів ігноруючи пунктуацію

        # Використовуємо regular expression для визначення мови
        # Також для оптимізації коду, використовуємо list comprehension
        ukrainian_words = [word for word in words if re.match(r'^[а-яА-Яієїґґ]+$', word)]
        english_words = [word for word in words if re.match(r'^[a-zA-Z]+$', word)]
        ukrainian_words.sort(key=custom_sort_key)
        english_words.sort(key=custom_sort_key)

        print("Слова українською мовою (відсортовані):", ukrainian_words)
        print("Слова англійською мовою (відсортовані):", english_words)
        print("Загальна кількість слів:", len(words))

except FileNotFoundError:
    print("Файл не знайдено.")
except Exception as e:
    print(e)
