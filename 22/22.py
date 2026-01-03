x = 0
y = 1
while (x:= x + 1) < 11 and (y:= y*2)< 100:
    print(f'x = {x}')
    print(f'y = {y}')

x = 0
while (x:= x + 1) < 11:
    if x == 5:
        continue # пропускаем print, вернуться к началу цикла
    print(f'x = {x}')

print('Done')

a = 1

b = 2
if a < b:
    pass  # заглушка, ничего не делать
else:
    print('a > b')


print(''' 
░██╗░░░░░░░██╗░█████╗░░██╗░░░░░░░██╗
░██║░░██╗░░██║██╔══██╗░██║░░██╗░░██║
░╚██╗████╗██╔╝██║░░██║░╚██╗████╗██╔╝
░░████╔═████║░██║░░██║░░████╔═████║░
░░╚██╔╝░╚██╔╝░╚█████╔╝░░╚██╔╝░╚██╔╝░
░░░╚═╝░░░╚═╝░░░╚════╝░░░░╚═╝░░░╚═╝░░''')

x = 1.2345
print(f'Значение х = {format(x, '0.2f')}')
print(f'Значение х = {x:.2f}')


with open ('text.txt') as file:
    for line in file:
        print(line, end='')



file = open('text.txt')
for line in file:
    print(line, end='')
file.close()