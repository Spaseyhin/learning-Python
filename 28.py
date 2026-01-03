arr = [1,3,4,5]

for i in arr:
    if i % 2 == 0:
        print(f'Найдены четное число {i}')
        break
else:
    print('Четных чисел нет')
