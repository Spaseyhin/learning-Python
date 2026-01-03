arr = [1,3,5,6]
position = 0
while position < len(arr):
    if arr[position] % 2 == 0:
        print(f'Найдено четное число {arr[position]}')
        break
    position += 1
else:
    print('Четных чисел не обнаружено')