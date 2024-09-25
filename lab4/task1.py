import csv
import random
from faker import Faker

fake = Faker(locale='uk_UA')

# Жіноча стать
f_users = []
for i in range(800):
    user = {
            'surname': fake.last_name_female(),
            'name': fake.first_name_female(),
            'middle_name': fake.middle_name_female(),
            'gender': "Жіноча",
            'birth_date': fake.date(),
            'job': fake.job(),
            'city': fake.city_name(),
            'address': fake.address(),
            'phone': fake.phone_number(),
            'email': fake.email()
        }
    f_users.append(user)

# Чоловіча стать
m_users = []
for i in range(1200):
    user = {
            'surname': fake.last_name_male(),
            'name': fake.first_name_male(),
            'middle_name': fake.middle_name_male(),
            'gender': 'Чоловіча',
            'birth_date': fake.date(),
            'job': fake.job(),
            'city': fake.city_name(),
            'address': fake.address(),
            'phone': fake.phone_number(),
            'email': fake.email()
        }
    m_users.append(user)

# Обʼєднання чоловіків та жінок в одну бібліотеку
all_users = f_users + m_users

# Перемішужмо у випадковій послідовності
random.shuffle(all_users)

# Записуємо бібліотеку у .csv файл
with open('employees.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Прізвище','Ім’я', 'По батькові', 'Стать',
                     'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання',
                     'Телефон', 'Email'])
    for user in all_users:
        writer.writerow([user['surname'], user['name'],user['middle_name'], user['gender'],
                         user['birth_date'], user['job'], user['city'], user['address'],
                         user['phone'], user['email']])
