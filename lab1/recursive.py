def fib (k):
    seq = []
    if k < 0:
        print('Невірний тип даних')
        return seq
    elif k == 0:
        return seq.append(0)
    elif k == 1:
        return seq.extend([0,1])
    else:
        seq.extend([0, 1])
        for i in range(2,k + 1):
          seq.append( seq [-1] + seq[-2])
    return seq
k = 10
print(f"Послідовність Фібоначчі ({k} перших цифр), є наступною: {fib(k)}" )
