import os
os.system('clear')
user_numbers_input = input('Enter numbers: ')
arr = user_numbers_input.split(' ')
new_arr = []
for i in arr:
    new_arr.append(int(i)**2)

new_tuple = tuple(new_arr)
print(f'The numbers were squared: {new_arr}')
print(f'The numbers were placed in a cartage: {new_tuple}')
sortedlist = tuple(sorted(set(user_numbers_input.split(' '))))

#The numbers were arranged in order and repetitions were removed
print(f'The numbers were arranged in order: {sortedlist}')
print(f'the tuple became a list: {list(sortedlist)}')