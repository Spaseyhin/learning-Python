import datetime

with open('habits.txt', 'aqt') as out:

    user_input = input('Введите строку')
    print(f'{user_input}', file=out)


