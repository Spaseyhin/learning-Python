import os
os.system('clear')
user_input_name  = input('Enter name: ')

user_input_name = user_input_name.split()
if len(user_input_name) == 2:
    print(f'{user_input_name[1].capitalize()}, {user_input_name[0].capitalize()}')
else:
    print('введите ровно два слова')