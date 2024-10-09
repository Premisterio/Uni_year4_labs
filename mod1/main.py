import json
import os
from math import isclose

# Код мови
ukrainian = 'uk'
english = 'en'

# Бібліотека мови інтерфейсу
lang_dictionary = {
    ukrainian: {
        'enter_sides': 'Введіть сторони трикутника a, b, c: ',
        'triangle_exists': 'Трикутник з сторонами {0}, {1}, {2} існує.',
        'right_triangle': 'Трикутник є прямокутним',
        'file_saved': 'Дані збережено в файл {0}',
        'triangle_not_exists': 'Трикутник з такими сторонами не існує.'
    },
    english: {
        'enter_sides': 'Enter the sides of the triangle a, b, c: ',
        'triangle_exists': 'The triangle with sides {0}, {1}, {2} exists.',
        'right_triangle': 'The triangle is a right triangle',
        'file_saved': 'Data saved to file {0}',
        'triangle_not_exists': 'A triangle with such sides does not exist.'
    }
}


def translate(text, language):
    return lang_dictionary.get(language, lang_dictionary[ukrainian]).get(text)


# Функція перевіряє чи сума двох введених сторін більша ніж третя сторона
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


# Функція що перевіряє чи введені сторони створюють трикутник, за допомогою теореми Піфагора
def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)


# Виводить дані про трикутник
def print_triangle_info(a, b, c, language):
    if is_triangle(a, b, c):
        print(translate('triangle_exists', language).format(a, b, c))
        if is_right_triangle(a, b, c):
            print(translate('right_triangle', language))
            hypotenuse = max(a, b, c)
            legs = sorted([a, b, c])[:2]
            print(f"Гіпотенуза: {hypotenuse}")
            print(f"Катет 1: {legs[0]}")
            print(f"Катет 2: {legs[1]}")
    else:
        print(translate('triangle_not_exists', language))


def main():
    file_name = 'MyData.json'

    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            try:
                data = json.load(f)
                a, b, c = data['sides']
                language = data['language']
            except (json.JSONDecodeError, KeyError, TypeError):
                get_user_input(file_name)
                return
    else:
        get_user_input(file_name)
        return

    # Якщо мова не розпізнана, вибираємо українську
    if language not in [ukrainian, english]:
        language = ukrainian
    print(f"Мова: {'Українська' if language == ukrainian else 'English'}")
    print_triangle_info(a, b, c, language)


def get_user_input(file_name):
    try:
        a = int(input("Введіть сторону a: "))
        b = int(input("Введіть сторону b: "))
        c = int(input("Введіть сторону c: "))
        language = input("Введіть мову інтерфейсу (uk/en): ")
    except Exception as e:
        print(e)
        return
    data = {
        'sides': [a, b, c],
        'language': language
    }

    with open(file_name, 'w') as f:
        json.dump(data, f)

    print(f"{translate('file_saved', language).format(file_name)}")


if __name__ == "__main__":
    main()