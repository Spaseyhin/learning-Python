print('q для выхода ) ')
while True:
    user_imput = input("Введите число: ")



    if user_imput == 'q':
        break
    user_imput = int(user_imput)


    if user_imput % 2 == 0:
        print(user_imput * user_imput)
    else:
        continue

    

