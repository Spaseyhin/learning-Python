import os
os.system('clear')
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])
print(color_list[1], color_list[-2])
print(list(reversed(color_list)))
#_________________________________________
for i in reversed(color_list):
    print(i)

max_len = 0
longest = ''
for i in color_list:
    if len(i) > max_len:
        max_len = len(i)
        longest = i
    
print(f'{longest} is longest')

#or

longest = max(color_list, key=len)
print(f'{longest} is longest')
#_________________________________________


color = input('Enter a color: ')
x = 0
for i in color_list:
    if  i == color:
        print(f'{color} is in the list')
        x += 1
if x == 0:
    print(f'{color} is not in the list')
#or

color = input('Enter a color: ').strip()

if color in color_list:
     print(f'{color} is in the list')
else:
     print(f'{color} is not in the list')


print()

if color in color_list:
    print(f'{color} is in the list')
else:
    print(f'{color} is not in the list')