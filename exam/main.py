import math
from deep_translator import GoogleTranslator

# Функція для перекладу тексту
def translate(text, lang_code):
    return GoogleTranslator(source='auto', target=lang_code).translate(text)

# Запит мови користувача
lang_code = input("Введіть код мови ('ukr' для української, 'eng' для англійської): ").strip()

# Тексти на двох мовах
texts = {
    "ukr": {
        "square_side": "Введіть сторону квадрата a: ",
        "circle_radius": "Введіть радіус кола R: ",
        "square_area": "Площа квадрата: ",
        "circle_area": "Площа кола: ",
        "larger_square": "Площа квадрата більше.",
        "larger_circle": "Площа кола більше."
    },
    "eng": {
        "square_side": "Enter the side of the square a: ",
        "circle_radius": "Enter the radius of the circle R: ",
        "square_area": "Square area: ",
        "circle_area": "Circle area: ",
        "larger_square": "The square area is larger.",
        "larger_circle": "The circle area is larger."
    }
}

# Вибір тексту відповідно до мови
if lang_code not in texts:
    lang_code = "ukr"  # Мова за замовчуванням

t = texts[lang_code]

# Введення даних
a = float(input(t["square_side"]))
R = float(input(t["circle_radius"]))

# Обчислення площ
square_area = a ** 2
circle_area = math.pi * R ** 2

# ANSI-код для червоного кольору
red = "\033[31m"
reset = "\033[0m"

# Виведення результатів
print(f"{t['square_area']} {red}{square_area:.2f}{reset}")
print(f"{t['circle_area']} {red}{circle_area:.2f}{reset}")

if square_area > circle_area:
    print(t["larger_square"])
else:
    print(t["larger_circle"])

