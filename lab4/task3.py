import matplotlib.pyplot as plt
from task2 import read_csv_file


#  Підрахунок статевого розподілу
def count_by_gender(employees):
    male_count = sum(1 for emp in employees if emp['gender'] == 'Чоловіча')
    female_count = sum(1 for emp in employees if emp['gender'] == 'Жіноча')

    print(f"Кількість чоловіків: {male_count}")
    print(f"Кількість жінок: {female_count}")

    if male_count == 0 and female_count == 0:
        print("Дані відсутні.")
        return

    labels = ['Чоловіки', 'Жінки']
    sizes = [male_count, female_count]
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['blue', 'pink'])
    plt.title('Статевий розподіл співробітників')
    plt.show()


#  Розподіл співробітників за статевою та віковою категорією
def count_by_age_category(employees):
    younger_18 = sum(1 for emp in employees if emp['age'] < 18)
    age_18_45 = sum(1 for emp in employees if 18 <= emp['age'] <= 45)
    age_46_70 = sum(1 for emp in employees if 46 <= emp['age'] <= 70)
    older_70 = sum(1 for emp in employees if emp['age'] > 70)

    print(f"Кількість молодших 18 років: {younger_18}")
    print(f"Кількість 18-45 років: {age_18_45}")
    print(f"Кількість 46-70 років: {age_46_70}")
    print(f"Кількість старших 70 років: {older_70}")

    labels = ['< 18', '18-45', '46-70', '> 70']
    sizes = [younger_18, age_18_45, age_46_70, older_70]
    plt.figure(figsize=(8, 6))
    plt.bar(labels, sizes, color=['green', 'blue', 'orange', 'red'])
    plt.title('Розподіл співробітників за віковими категоріями')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.show()


#  Розподіл співробітників за статею та віковою категорією
def count_by_gender_and_age(employees):
    categories = {
        '< 18': {'Чоловіча': 0, 'Жіноча': 0},
        '18-45': {'Чоловіча': 0, 'Жіноча': 0},
        '46-70': {'Чоловіча': 0, 'Жіноча': 0},
        '> 70': {'Чоловіча': 0, 'Жіноча': 0},
    }

    for emp in employees:
        age = emp['age']
        gender = emp['gender']
        if age < 18:
            categories['< 18'][gender] += 1
        elif 18 <= age <= 45:
            categories['18-45'][gender] += 1
        elif 46 <= age <= 70:
            categories['46-70'][gender] += 1
        else:
            categories['> 70'][gender] += 1

    for category, counts in categories.items():
        print(f"Вікова категорія {category}: Чоловіків = {counts['Чоловіча']}, Жінок = {counts['Жіноча']}")

    labels = list(categories.keys())
    male_counts = [categories[label]['Чоловіча'] for label in labels]
    female_counts = [categories[label]['Жіноча'] for label in labels]
    width = 0.35
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(labels, male_counts, width, label='Чоловіки', color='blue')
    ax.bar(labels, female_counts, width, bottom=male_counts, label='Жінки', color='pink')
    ax.set_xlabel('Вікова категорія')
    ax.set_ylabel('Кількість')
    ax.set_title('Розподіл співробітників за статево-віковою категорією')
    ax.legend()
    plt.show()


csv_file_path = 'employees.csv'
employees = read_csv_file(csv_file_path)
count_by_gender(employees)
count_by_age_category(employees)
count_by_gender_and_age(employees)


