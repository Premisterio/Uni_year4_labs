import psycopg2
from prettytable import PrettyTable

# Підключення до БД
conn = psycopg2.connect(
    dbname="my_db",
    user="admin",
    password="admin",
    host="db",
    port="5432"
)
cursor = conn.cursor()

# Створення таблиць
cursor.execute("""
CREATE TABLE IF NOT EXISTS Suppliers (
    supplier_id SERIAL PRIMARY KEY,
    company_name TEXT NOT NULL,
    contact_person TEXT,
    phone VARCHAR(15),
    account_number TEXT
);

CREATE TABLE IF NOT EXISTS Materials (
    material_id SERIAL PRIMARY KEY,
    material_name TEXT NOT NULL,
    price NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS Supplies (
    supply_id SERIAL PRIMARY KEY,
    supply_date DATE NOT NULL,
    supplier_id INT REFERENCES Suppliers(supplier_id),
    material_id INT REFERENCES Materials(material_id),
    delivery_days INT CHECK (delivery_days BETWEEN 1 AND 7),
    quantity INT NOT NULL
);
""")
conn.commit()

# Заповнення таблиць даними
cursor.execute("""
INSERT INTO Suppliers (company_name, contact_person, phone, account_number) VALUES
('Wood Inc.', 'John Doe', '123-456-7890', 'UA123456'),
('Metal Corp.', 'Jane Smith', '098-765-4321', 'UA654321'),
('Paint Co.', 'Bob Ross', '555-555-5555', 'UA987654'),
('Supplies Ltd.', 'Alice Johnson', '111-222-3333', 'UA111222');

INSERT INTO Materials (material_name, price) VALUES
('Wood', 50.00),
('Steel Parts', 150.00),
('Lacquer', 25.00);

INSERT INTO Supplies (supply_date, supplier_id, material_id, delivery_days, quantity) VALUES
('2024-11-10', 1, 1, 3, 100),
('2024-11-11', 2, 2, 7, 50),
('2024-11-12', 3, 3, 2, 200);
""")
conn.commit()

# Виведення даних з таблиць
tables = ["Suppliers", "Materials", "Supplies"]

for table in tables:
    cursor.execute(f"SELECT * FROM {table};")
    rows = cursor.fetchall()
    table_print = PrettyTable()
    table_print.field_names = [desc[0] for desc in cursor.description]
    for row in rows:
        table_print.add_row(row)
    print(f"Таблиця {table}:\n{table_print}\n")

# Запити
# Поставки за 3 дні або менше
cursor.execute("""
SELECT * FROM Supplies 
JOIN Suppliers ON Supplies.supplier_id = Suppliers.supplier_id 
WHERE delivery_days <= 3
ORDER BY company_name;
""")
rows = cursor.fetchall()
print("Поставки за 3 дні або менше:")
for row in rows:
    print(row)

conn.close()
