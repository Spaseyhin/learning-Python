import os

os.system('clear')

user_input_numders = input('Enter numbers: ')
list_numbers = user_input_numders.split(' ')
tuple_numbers = tuple(list_numbers)

print(f'''tuple_numbers: {tuple_numbers} is {type(tuple_numbers)}
list_numbers: {list_numbers} is {type(list_numbers)}''')


