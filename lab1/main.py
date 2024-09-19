while True:
    try:
        a = int(input('Введіть перше число: '))
        b = int(input('Введіть друге число: '))
        break
    except ValueError:
        print('Введений невірний тип даних')
if a > b:
    a, b = b, a
print('Прості числа між ', a , ' та ', b,':')

def is_prime(n):
    lst = []
    for j in range(n-1, 1, -1):
        if n % j == 0:
            lst.append(j)

    if len(lst) == 0:
        return True
    else:
        return False

for i in range(a, b + 1):
    if is_prime(i):
        print(i)
