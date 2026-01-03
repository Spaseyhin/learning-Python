import os
os.system('clear')

file_name = input('Enter name of file: ')
result_1 = file_name.split('.')[-1]


result_2 = file_name.split('.')[0]

print(result_1, result_2)

if result_1 == 'txt':
    print(f"the file extension is txt")
elif result_1 == 'py':
    print(f"the file extension is py")
elif result_1 == 'csv':
    print(f"the file extension is csv")
else:
    print(f"the file extension is unknown")